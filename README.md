# Car Price Prediction Using Machine Learning

Welcome to the Car Price Prediction project! This repository contains the code and resources used to predict car prices based on various features using machine learning techniques.

## Project Overview

This project aims to predict the selling price of cars using a dataset from Kaggle. The dataset contains various features of cars such as age, mileage, fuel type, seller type, transmission type, and more. Multiple machine learning algorithms were used to build and evaluate models to achieve accurate predictions.

![Car Price Prediction](https://github.com/user-attachments/assets/84a9af96-c8b6-406d-8ca9-0c8a83e735d5)

## Dataset

The dataset used in this project is obtained from Kaggle. You can find it [here](https://www.kaggle.com/nehalbirla/vehicle-dataset-from-cardekho).

## Project Structure

The repository contains the following files and directories:

- `CarPricePrediction.ipynb`: Jupyter notebook containing the code for data preprocessing, model building, and evaluation.
- `car_price_prediction_model.pkl`: Trained Random Forest model saved using joblib.
- `README.md`: Project overview and documentation.
- `requirements.txt`: List of Python packages required to run the project.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.6 or higher
- Jupyter Notebook
- Required Python packages (listed in `requirements.txt`)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/harishsemwal/CarPricePrediction.git
    cd CarPricePrediction
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Jupyter notebook:
    ```bash
    jupyter notebook CarPricePrediction.ipynb
    ```

## Data Preprocessing

The data preprocessing steps include:

- Importing necessary libraries and the dataset.
- Exploring the dataset for understanding and identifying missing values.
- Dropping irrelevant columns.
- Creating new features such as the car's age.
- Encoding categorical variables using one-hot encoding.
- Visualizing correlations between features and the target variable.

## Model Building

Several machine learning algorithms were used to build the prediction models:

1. **Linear Regression**
2. **Multiple Linear Regression**
3. **Random Forest Regressor**
4. **Decision Tree Regressor**

## Model Evaluation

Each model was evaluated using the R-squared score to determine its performance. The results were as follows:

- **Random Forest Regressor**: 95% accuracy
- **Decision Tree Regressor**: 94% accuracy
- **Multiple Linear Regression**: 91% accuracy

## Visualizations

### Multiple Linear Regression
![MLR](https://github.com/user-attachments/assets/6c590ee4-3af9-49a7-bc26-1481085f81e6)

### Random Forest Regressor
![RF](https://github.com/user-attachments/assets/bf2f39b3-5e2f-423c-8a71-1708f2565716)

### Decision Tree Regressor
![Screenshot 2024-07-20 091006](https://github.com/user-attachments/assets/21b67108-42a8-446c-a511-2dbb7457964d)

## Hyperparameter Tuning

RandomizedSearchCV was used to find the optimal parameters for the Random Forest Regressor to improve its performance.

## Results

The final model, Random Forest Regressor, was trained with the optimal parameters and achieved a high R-squared score on the test data.

## Future Work

- Incorporating additional features like car brand and model.
- Exploring advanced machine learning algorithms like Gradient Boosting and XGBoost.
- Enhancing data quality by collecting more recent car listings.
- Deploying the model in a web application for real-time predictions.
- Applying advanced feature engineering techniques.

## Conclusion

This project successfully demonstrated the use of machine learning algorithms to predict car prices. The Random Forest Regressor provided the best performance among the models tested. Future enhancements can further improve the accuracy and usability of the model.

## Contributing

Feel free to fork this repository and contribute by submitting a pull request. For major changes, please open an issue to discuss what you would like to change.

## License

This project is licensed under the MIT License.

## Acknowledgments

- Thanks to Kaggle for providing the dataset.
- Special thanks to all the contributors of the libraries used in this project.

---

**Developed by Harish Prasad Semwal**  
**Email:** harishsemwal581@gmail.com
