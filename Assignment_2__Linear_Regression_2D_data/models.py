import numpy as np

class linear_model:
    '''
    Linear model class is used to create the regression model that is used in the 
    assignment. 
    It has three data elements:
    W: Stores the weight vector for the linear regression (plus one term for bias, using the bias trick) # Search for 'bias trick' in 'http://cs231n.github.io/linear-classify/'
    lr: learning rate for the gradient descent update equation
    LIST_W: Stores the weight vector after each update (used later to show how weights change after each epoch)

    It has three functions:
    forward(): it calculates the predicted output by the model for given input points
    backward(): it performs the weight update by gradient descent 
    loss(): it computes the Euclidean loss between the predicted and the actual values corresponding to the input data points
    '''
    
    def __init__(self, W_size, lr, init='random'):
        '''
        Initializes an object of the linear_model class.

        INPUT:
        -----
        It has three inputs:
        W_size: an integer equal to the feature_size + 1 (for bias)
        lr: the learning rate to be used in weight update during gradient descent
        init: method for initialization of weight matrix
        '''
        
        self.lr = lr
        if init == 'random': # initialize the weight matrix with random values
            self.W = np.random.random((W_size, 1))
        elif init == 'zeros': # initialize the weight matrix with zero values
            self.W = np.zeros((W_size, 1))
        else:
            raise Exception
        self.LIST_W = np.zeros((W_size, 0))

    def forward(self, feat):
        '''
        This function calculates the predicted output by the model for given input points.

        INPUT:
        -----
        It takes as input a numpy 2D array 'feat' of dimensions [(number of data points) x (size of feature for each data point)].

        For example: Consider the following data points: (x1: 0.1, y1: 1), (x2: 0.4, y1: 4).
        Let us have the following features corresponding to each of the data points:
        x1: f1 -> (3, 4)
        x2: f2 -> (6, 5)

        Then the feat matrix would be:
        np.array([[3, 4],
                  [6, 5]])


        OUTPUT:
        ------
        The output of this function is a numpy 2D array 'y_pred' of dimensions [(number of data points) x 1]. It contains the values predicted by the function forward().

        For example: In the above example y_pred could be:
        np.array([[3],
                  [2]])

        '''

        y_pred=feat.dot(self.W)
    

        ### YOUR CODE SHOULD END HERE ###
        
        return y_pred

    def backward(self, y_actl, y_pred, feat):
        '''
        This function performs the weight update by gradient descent.
        
        INPUT:
        -----
        It takes three inputs:
        feat: same as described in forward()
        y_pred: same as described in forward()
        y_actl: is a numpy 2D array of dimensions [(number of data points) x 1]. It contains the actual values corresponding to the data points. 

        In the example given in the forward() function, y_actl would be:
        np.array([[1],
                  [4]])
        
        OUTPUT:
        ------
        This function has NO output.

        FUNCTION:
        --------
        It updates the self.W matrix according to the gradient descent rule (for help refer HINT.pdf).

        '''
        m=y_pred.size 
        self.W=self.W-1/m*self.lr*(feat.T).dot(y_pred-y_actl)                                                                 
            
        

        ### YOUR CODE SHOULD END HERE ###

        # store the updated weight vector in the list
        self.LIST_W = np.append(self.LIST_W, self.W, 1)


    def loss(self, y_actl, y_pred):
        '''
        This function computes the Euclidean loss between the predicted and the actual values corresponding to the input data points
        
        INPUT:
        -----
        It takes two inputs:
        y_pred: same as described in forward()
        y_actl: same as described in backward()
        
        OUTPUT:
        ------
        This function has a single scalar (float variable 'scalar_LOSS') as its output. This represents the Euclidean loss between the predicted and actual values.
        '''

        loss=y_pred-y_actl
        m=y_actl.size
        scalar_LOSS=1/(2*m)*np.sum(np.multiply(loss,loss))
        

        ### YOUR CODE SHOULD END HERE ###

        return scalar_LOSS

    
def calc_features(X, choice, param=5):
    '''
    This function computes the features for the data points and packs all the data points into a single 
    
    INPUT:
    -----
    It takes three inputs:
    X: this is a numpy 2D array of dimension [(number of data points) x 1]. It contains the data points corresponding to the data.
    In the example used in forward() function of the linear_model class, X would be:
    np.array([[0.1],
              [0.4]])

    choice: specifies the type of features to be used to represent the data points (see the function body for more details)
    param: attribute that specifies some aspect depending on the type of the feature extraction mechanism (see the function body for more details)

    OUTPUT:
    ------
    This function has a single output 'feat'. 'feat' is a numpy 2D array (same as that described in forward() function of the linear_model class.
    '''
    
    feat = []
    for x in X:
        if choice == 'linear':

            # 'linear' option outputs the input as the sole feature.
            #
            # E.g.: if x = np.array([[3],
            #                        [2]])
            # then feat should be np.array([[3, 1],
            #                               [2, 1]])
            # i.e. features are same as input AND 1 is added for the bias trick (see above)

            

            feat=np.append(feat,np.vstack((x,np.ones_like(1)))).reshape(-1,2)
            
            ### YOUR CODE SHOULD END HERE ###

        elif choice == 'poly':

            # 'poly' option calculates multiplicative features
            # here param option is used to represent the (one plus the) degree of the polynomial
            #
            # E.g.: if x = np.array([[3],
            #                        [2]])
            # param = 3 means that the polynomial should be quadratic (of degree 2)
            # The feature vector in this case would be [x^2, x^1, x^0]
            #
            # feat should be np.array([[9, 3, 1, 1],
            #                          [4, 2, 1, 1]])
            # i.e. features are powers of input AND 1 is added for the bias trick (see above)
            a=[] 
            for i in reversed(range(param)):
                a.append(x**i)
            a.append(1)    
            feat=np.append(feat,a).reshape(-1,param+1)
            
            
            ### YOUR CODE SHOULD END HERE ###

        elif choice == 'fourier':

            # 'fourier' option calculates sin(nx) and cos(nx) features for representing periodic functions
            # here param option is used to represent the number of pairs of sin(x), cos(x)
            #
            # see for details: 'http://mathworld.wolfram.com/FourierSeries.html'
            #
            # E.g.: if x = np.array([[3],
            #                        [2]])
            # param = 2 means that the feature should consist of sin(1*x), cos(1*x), sin(2*x), cos(2*x)
            # The feature vector in this case would be [sin(1*x), cos(1*x), sin(2*x), cos(2*x)]
            #
            # feat should be np.array([[sin(1*3), cos(1*3), sin(2*3), cos(2*3), 1],
            #                          [sin(1*2), cos(1*2), sin(2*2), cos(2*2), 1]])
            # i.e. features are sin and cos of input AND 1 is added for the bias trick (see above)
           
            a=[]
            for i in reversed(range(param)):
                a.append(np.sin((i+1)*x))
                a.append(np.cos((i+1)*x))
            a.append(1)                   
            feat=np.append(feat,a).reshape(-1,2*param+1)

            ### YOUR CODE SHOULD END HERE ###

        
        elif choice == 'your_own_features':

            # You can create your own features here

            a=[]
            for i in reversed(range(param)):
                a.append(x**i)
            a.append(np.sin(x))
            a.append(np.cos(x))
            a.append(1)
            feat=np.append(feat,a).reshape(-1,param+3)

            ### YOUR CODE SHOULD END HERE ###

            
    ### ANY ADDITIONAL CODE SHOULD BEGIN HERE ###

            
    
    
    return feat
