# loan_classification
Creating various ML Models to classify consumer data for loan approval.

Kaggle dataset -> https://www.kaggle.com/ajay1735/hmeq-data

### Context
The consumer credit department of a bank wants to automate the decisionmaking process for approval of home equity lines of credit. To do this, they will follow the recommendations of the Equal Credit Opportunity Act to create an empirically derived and statistically sound credit scoring model. The model will be based on data collected from recent applicants granted credit through the current process of loan underwriting. The model will be built from predictive modeling tools, but the created model must be sufficiently interpretable to provide a reason for any adverse actions (rejections).

### Content
The Home Equity dataset (HMEQ) contains baseline and loan performance information for 5,960 recent home equity loans. The target (BAD) is a binary variable indicating whether an applicant eventually defaulted or was seriously delinquent. This adverse outcome occurred in 1,189 cases (20%). For each applicant, 12 input variables were recorded.

## Models used
* Logistic Regression
* Random Forest

## Results
#### Random Forest Classifier
<img width="309" alt="Screen Shot 2022-07-03 at 4 29 07 PM" src="https://user-images.githubusercontent.com/25440531/177056231-a56ffcd0-d583-4ff1-afef-3a2c54bc992b.png">

* With Cross Validation
<img width="402" alt="image" src="https://user-images.githubusercontent.com/25440531/177056239-c205e384-75f9-4aaa-9a55-e70d1c4ce85e.png">

* Confusion Matrix:
<img width="81" alt="image" src="https://user-images.githubusercontent.com/25440531/177056253-31d7bdfd-4210-4d93-aab0-e929ecd186d6.png">


#### Logistic Regression
<img width="312" alt="Screen Shot 2022-07-03 at 4 29 55 PM" src="https://user-images.githubusercontent.com/25440531/177056259-65eff04c-7cf5-4588-b452-47c1ed013e17.png">

* With Cross Validation
<img width="339" alt="image" src="https://user-images.githubusercontent.com/25440531/177056261-17ea04f1-8757-4feb-9ec4-ef6b1e879309.png">

* Confusion Matrix:
<img width="89" alt="Screen Shot 2022-07-03 at 4 30 35 PM" src="https://user-images.githubusercontent.com/25440531/177056271-a2ff0ce3-900a-4fb4-9015-3764d5f070bf.png">
