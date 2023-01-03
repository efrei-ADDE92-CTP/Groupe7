# import libraries
import pandas as pd
from sklearn.datasets import load_iris 


def load_iris_dataset():
    iris = load_iris()
    # create dataframe
    import pandas as pd
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    df['target_names'] = df.target.apply(lambda x: iris.target_names[x])
    return df
