library(ggbiplot)

# LOAD THE DATA
data <- read.table('NC_001416.aa', sep='\t', header=TRUE)

# STRIP OUT ONLY THE COUNTS
dat <- data[,unlist(strsplit("ARNDCEQGHILKMFPSTWYV", ""))]

# DIVIDE BY THE ROW SUMS TO GET THE FREQUENCY
dat.norm <- dat/rowSums(dat)

# SCALE THE VALUES
dat.scaled <- scale(dat.norm)

# CLASSIFY EACH ROW USING KMEANS
clust <- kmeans(dat.scaled, 2)$cluster

# CALCULATED THE PCA
dat.pca <- prcomp(dat.scaled, center = FALSE, scale. = FALSE)

# PLOT
g <- ggbiplot(dat.pca, 
			  groups = as.factor(data$TYPE), 
			  varname.size = 5, 
			  obs.scale = 3, 
			  var.scale = 1, 
			  ellipse = TRUE, 
			  circle = FALSE, 
			  alpha = 1
			  )
# LEGEND
g <- g + theme(legend.direction = 'vertical', 
	legend.justification=c(0,1), 
	legend.position=c(0.8, 0.95),
	legend.background = element_rect(linetype = 2, size = 0.5, colour = 1)),
	legend.key = element_blank()
	)
# OPTIONS
g <- g + geom_point(aes(colour=as.factor(clust), shape=as.factor(clust)), size=3, pch=22, alpha=1 )
g <- g + ggtitle("amino-acid frequency of potential ORFs from Lambda phage")
g <- g + theme(plot.title = element_text(hjust = 0.5))
g <- g + guides(color=guide_legend(title="TYPE")) 
#g <- g + scale_color_manual(name="TYPE", values=c("blue", "red", "blue", 'red'))
#g <- g + xlim(-6, 6) + ylim(-6, 6)
#print(g)

# CREATE TIFF IMAGE
tiff(filename="figure.tiff", width=8, height=6, units="in", res=200)
print(g)
invisible(dev.off())
cat("Output image: figure.tiff\n")



