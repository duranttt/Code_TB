### Receiver operator characteristics and precision-recall curves
### U. Braunschweig, University of Toronto, 08/2020


getAUC <- function(real, pred, returnRates=T, seed=NULL) {
### Compute true positive rate, false positive rate and precison
### as well as AUROC (area under the revceiver operator characteristics curve)
### and AUPRC (area under the precision recall curve)
###
### Parameters:
### - real: Ground-truth state of observations (TRUE or FALSE)
### - pred: Value of predictor, e.g. classifier (real number in [0,1])
### - returnRates: Return the tableof TRP, FPR and precision
### - seed: When multiple observations have the same pred value,
###         they are shuffled randomly. A seed can be provided to produce
###         reproducible results.
### Value: AUROC if returnRates=FALSE, and a list with AUROC, AUPRC and
###   a table of predictor increments, TPR, FPR and precision
   
    set.seed(seed)
    rates <- cbind(real = as.logical(real), pred=pred)[
        order(pred, sample(1:length(pred)), decreasing=T),] # to destroy pre-sort
    rates <- rates[!is.na(rowSums(rates)),]
    rates <- cbind(rates,
                 TP   = cumsum(rates[,"real"]),
                 FP   = cumsum(!rates[,"real"])                 
                 )
    rates <- cbind(rates,
                 TPR  = rates[,"TP"] / sum(rates[,"real"]),
                 FPR  = rates[,"FP"] / length(which(rates[,"real"] == 0)),
                 prec = rates[,"TP"] / 1:nrow(rates)
                 )
    rates <- rates[,-c(1,3,4)]
    rates <- rbind(c(pred=1, TPR=0, FPR=0, prec=1),
                 rates,
                 c(pred=0, TPR=1, FPR=1, prec=0)
                 )

    auroc <- sum(((rates[-nrow(rates),"TPR"] + rates[-1,"TPR"]) / 2) *
                 (rates[-1,"FPR"] - rates[-nrow(rates),"FPR"]))
    auprc <- sum(((rates[-nrow(rates),"prec"] + rates[-1,"prec"]) / 2) *
                 (rates[-1,"TPR"] - rates[-nrow(rates),"TPR"]))

    if (returnRates) {
        return(list(AUROC     = auroc,
                    AUPRC     = auprc,
                    rates     = rates)
               )
    } else {
        return(auroc)
    }
}


plotROC <- function(auc, main="", addInfo=FALSE, maxFPR=1, minPrec=0) {
### Plot TPR vs. FPR and optinoally find cutoff with largest spread
### and satisfying maxFPR and minPrec.
###
### Parameters:
### - auc: List containing a slot $rates with columns 'pred' (the value of a model such as
###        a classifier), 'TPR', 'FPR' and 'prec'. Can be produced with getAUC().
### - main: Plot title
### - addInfo (logical): Whether or not to attempt to find an optimal cutoff, i.e.
###        one that maximizes the difference of TPR-FPR, that also satisfies maxFPR
###        and minPrec.
### - maxFPR: The maximum FPR for an optimal
### Value: This function is invoked mainly for generating a ROC plot. If addInfo=TRUE,
###        returns the cutoff with associated metrics.
    
    plot(auc$rates[,c("FPR","TPR")], xaxs="i", yaxs="i", type="l", lwd=3,
         main=main)
    abline(a=0, b=1, lty=2)
    text(0.65, 0.35, labels=round(auc$AUROC, 2), cex=1.5)

    if (addInfo) {
        eligOpt  <- which(auc$rates[,"FPR"] <= maxFPR & auc$rates[,"prec"] >= minPrec)
        whichOpt <- eligOpt[which.max(auc$rates[eligOpt,"TPR"] - auc$rates[eligOpt,"FPR"])]
        
        points(auc$rates[whichOpt, "FPR"], auc$rates[whichOpt, "TPR"], 
               pch=19, cex=1.5, col="dodgerblue")
        text(auc$rates[whichOpt, "FPR"], auc$rates[whichOpt, "TPR"], adj=c(-0.2,1.8),
             c(paste("P =", signif(auc$rates[whichOpt,"pred"],2)))
             )
        
        return(auc$rates[whichOpt,])
    }
}


plotPRC <- function(auc, main="", addInfo=FALSE) {
### Plot precision-recall curve and optionally cutoff with highest F1 score.
###
### Parameters:
### - auc: List containing a slot $rates with columns 'pred' (the value of a model such as
###        a classifier), 'TPR', 'FPR' and 'prec'. Can be produced with getAUC().
### - main: Plot title
### - addInfo (logical): Whether or not to attempt to find an optimal cutoff, i.e.
###        one that maximizes F1 score.
### Value: This function is invoked mainly for generating a precision-recall plot.
###        If addInfo=TRUE, returns the cutoff with associated metrics.

    plot(auc$rates[,c("TPR","prec")], xaxs="i", yaxs="i", type="l", lwd=3,
         xlab="Recall", ylab="Precision",
         main=main)
    text(0.35, 0.35, labels=round(auc$AUPRC, 2), cex=1.5)

    if (addInfo) {
        f1score   <- 2 * auc$rates[,"TPR"] * auc$rates[,"prec"] /
                        (auc$rates[,"TPR"] + auc$rates[,"prec"])
        whichOpt <- which.max(f1score)               

        caption <- paste0("P = ", signif(auc$rates[whichOpt,"pred"],2),
                          ", F1 = ", signif(f1score[whichOpt],2))
        points(auc$rates[whichOpt, "TPR"], auc$rates[whichOpt, "prec"],
               pch=19, cex=1.5, col="dodgerblue")
        text(auc$rates[whichOpt, "TPR"], auc$rates[whichOpt, "prec"], adj=c(1.1,1.5),
             caption
             )
        
        return(c(auc$rates[whichOpt,], F1score=f1score[whichOpt]))
    }
}




