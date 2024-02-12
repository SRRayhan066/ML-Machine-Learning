## Data preprocessing
The library pandas are mainly used for data manipulation. For importing-
```
import pandas as pd
```
For filling up missing values based on mean,median or mode of a dataset, there is a term called <b>imputer</b> in scikit-learn library. For using-
```
from sklearn.impute import SimpleImputer
```
After that, filling up the missing data based on mean-
```
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
```
Based on median-
```
imputer = SimpleImputer(missing_values=np.nan, strategy='median')
```
Based on mode-
```
imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
```

For transfarring string value to numerical value-
```
from sklearn.preprocessing import LabelEncoder
labelEncoder_X = LabelEncoder()
X.iloc[:,0] = labelEncoder_X.fit_transform(X.iloc[:,0])
```
