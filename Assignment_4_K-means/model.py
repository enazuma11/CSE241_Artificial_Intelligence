"""
model.py

This file implements the Logistic Regression model for classification.
"""

import numpy as np

class Kmeans(object):

    def __init__(self, dist = 'euc'):
        """
        Initialise the model. Here, we only initialise the weights as 'None',
        as the input size of the model will become apparent only when some
        training samples will be given to us.

        @add_bias: Whether to add bias.
        """

        # Initialise model parameters placeholders. Don't need another placeholder
        # for bias, as it can be incorporated in the weights matrix by adding
        # another feature in the input vector whose value is always 1.
        self.n_clusters = None
        self.n_data_points = None
        self.n_dimensions = None
        self.n_iterations = None

        self.centers = None
        self.labels = None
        self.dist = dist

    def distance(self, a, b):
        if(self.dist == 'euc'):
            return self.euc(a,b)

    def euc(self,a,b):
        ''' Input - @a, @b are two vectors
            Output - return a single value which is the difference of @a and @b
        '''
        dist = np.linalg.norm(a-b,axis=1)
        return dist
        
    
      

    def cluster(self, X, k = 1, n_iter = 10, debug = True):
        self.n_clusters = k
        self.n_iterations = n_iter
        self.n_data_points = X.shape[0]
        self.n_dimensions = X.shape[1]

        # INITIALIZATION
        self.centers = np.random.randn(self.n_clusters,self.n_dimensions)
        
        '''
        Pick @k cluster centers randomly from the data points (@X) and store the sampled points in a variable called @self.centers
        '''
        ''' YOUR CODE HERE'''
        '''idx=np.random.randint(self.n_data_points,size=self.n_clusters)
        self.centers=X[idx,:]'''
        for i in range(self.n_clusters):
            self.centers[i]=X[i]
        
        ''' YOUR CODE ENDS'''
        

        self.labels = np.zeros(self.n_data_points)
        '''
            Update the cluster centers now.
        '''
        ''' YOUR CODE HERE'''
        for i in range(self.n_iterations):
            for j in range(self.n_data_points):
                distances=self.distance(X[j],self.centers)
                min_dist=np.argmin(distances)
                self.labels[j]=min_dist
            for l in range(self.n_clusters):
                points = [X[t] for t in range(len(X)) if self.labels[t] == l]
                self.centers[l]=np.mean(points,axis=0)
                                            
           
                    
        
        # Loop here.
        
            # Allocate label to each document
        
        
            # Find new cluster centers
        
        ''' YOUR CODE ENDS'''

        return self.labels
