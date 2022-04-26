library(party)
arg <- commandArgs(T)

trainData <- read.table(arg[1] , sep="\t", header=TRUE)

trainData$Result <- factor(trainData$Result, levels = c(0,1),  labels = c('negtive','positive'))

myFormula <- Result ~ Total + Mycobacterium + Complex + Complex_RPM + Ratio

iris_ctree <- ctree(myFormula, data=trainData )

print(iris_ctree)


pdf(arg[2])
plot(iris_ctree)
dev.off()
