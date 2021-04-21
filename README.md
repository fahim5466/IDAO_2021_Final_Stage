# IDAO 2021 Finals - Final Submission

### This is the final submission that gave us our highest score in public LB. Our final score was 3436.63 out of 6750 and we were 26th among the 32 participant teams.

## Files to add:
We used the original trxn.csv, aum.csv, client.csv and funnel.csv files. You have to copy the original csv files (trxn.csv, aum.csv, client.csv and funnel.csv) to the "tests/train_data_sample" folder.

## TLDR; running train script and submitting solution
1. Run `docker-compose -f docker-compose.train.yaml up`. This should produce a `submission/model.joblib` file with trained model and a tar archive with your model in `generated_submissions` folder. First time docker-compose could run for some time to build the docker image. Next time it will be much quicker.
2. Run `docker-compose -f docker-compose.test.yaml up`. This will produce a .csv file with your predictions in `generated_submissions` folder.
