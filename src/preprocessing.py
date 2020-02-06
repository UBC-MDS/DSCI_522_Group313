# authors: Suvarna Moharir, Jaekeun Lee, Chimaobi Amadi
# date: 2020.01.24

''' This script reads in the data, drops blank columns, cleans missing data, and then splits the data into testing and training sets
Usage: preprocessing.py [--quebec_path=<quebec_path> --store_path=<store_path>]

Options:
--quebec_path=<quebec_path> Relative file path for the quebec_df csv  [default: data/raw_quebec_city_airbnb_data.csv]
--store_path=<store_path>   Full path and file name to where the processed data should live and called [default: data/cleaned_data.csv]
'''

#importing packages and libraries
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from docopt import docopt

opt = docopt(__doc__)

def main(quebec_path, store_path):
    file = pd.read_csv(quebec_path)

    #dropping columns where all values are null and/or columns that are in French
    quebec_df = file.drop(columns = ['summary', 'space', 'listing_url', 'host_url', 'description', 'scrape_id', 'last_scraped', 'experiences_offered','thumbnail_url', 'medium_url', 'xl_picture_url', 'host_acceptance_rate', 'name', 'neighbourhood', 'neighborhood_overview', 'neighbourhood_group_cleansed', 'host_neighbourhood', 'jurisdiction_names', 'license', 'cancellation_policy', 'notes', 'transit', 'access', 'interaction', 'house_rules', 'picture_url', 'host_about', 'host_thumbnail_url', 'host_total_listings_count', 'minimum_minimum_nights', 'minimum_maximum_nights', 'maximum_maximum_nights', 'maximum_minimum_nights', 'minimum_nights_avg_ntm', 'maximum_nights_avg_ntm', 'host_picture_url', 'host_name', 'host_since', 'host_location', 'host_verifications', 'state', 'street', 'market', 'smart_location', 'country_code', 'country','amenities', 'calendar_updated', 'calendar_last_scraped', 'first_review', 'last_review', 'square_feet', 'weekly_price', 'monthly_price', 'security_deposit', 'cleaning_fee', 'zipcode', 'id', 'host_id', 'neighbourhood_cleansed', 'city'])

    #dropping all NaN-containing rows
    quebec_df = quebec_df.dropna()

    #making sure there are no missing values and dataframe has the correct dimensions
    assert quebec_df.columns[quebec_df.isna().any()].tolist() == [], "There are still missing values"
    assert quebec_df.shape[0] == 2194, "Wrong number of rows"
    assert quebec_df.shape[1] == 45, "Wrong number of columns"

    #removing '$' from price and fees and converting string to float
    quebec_df.price = quebec_df.price.replace('[\$,]', '', regex=True).astype(float)
    quebec_df.extra_people = quebec_df.extra_people.replace('[\$,]', '', regex=True).astype(float)

    #changing response rate from string to numeric and removing '%' sign
    quebec_df.host_response_rate = quebec_df['host_response_rate'].str.rstrip('%').astype('float')

    #changing booleans 'True' and 'False' to 1 and 0
    quebec_df.host_is_superhost = quebec_df.host_is_superhost.replace({True: 1, False: 0})
    quebec_df.host_has_profile_pic = quebec_df.host_has_profile_pic.replace({True: 1, False: 0})
    quebec_df.host_identity_verified = quebec_df.host_identity_verified.replace({True: 1, False: 0})
    quebec_df.is_location_exact = quebec_df.is_location_exact.replace({True: 1, False: 0})
    quebec_df.has_availability = quebec_df.has_availability.replace({True: 1, False: 0})
    quebec_df.requires_license = quebec_df.requires_license.replace({True: 1, False: 0})
    quebec_df.instant_bookable = quebec_df.instant_bookable.replace({True: 1, False: 0})
    quebec_df.is_business_travel_ready = quebec_df.is_business_travel_ready.replace({True: 1, False: 0})
    quebec_df.require_guest_profile_picture = quebec_df.require_guest_profile_picture.replace({True: 1, False: 0})
    quebec_df.require_guest_phone_verification = quebec_df.require_guest_phone_verification.replace({True: 1, False: 0})

    #making sure that the datatypes oot converted properly
    assert quebec_df.dtypes.price == 'float64',  "price string to float conversion did not convert properly"
    assert quebec_df.dtypes.host_response_rate == 'float64', "host_reponse_rate string to float did not convert properly"
    assert quebec_df.dtypes.host_is_superhost == 'int64', "host_is_superhost boolean to number did not convert properly"

    #making an 80-20 train-test split
    X = quebec_df.drop(columns = ['price'])
    y = quebec_df[['price']]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 5)

    #making sure split sizes are correct
    assert X_train.shape[1] == 44, "X_train did not split properly"
    assert y_train.shape[1] == 1, "y_train did not split properly"

    #assigning categorical and numeric features
    categorical_features = ['host_response_time', 'property_type', 'room_type', 'bed_type']
    numeric_features = ['host_response_rate', 'host_is_superhost', 'host_listings_count', 'host_has_profile_pic', 'host_identity_verified', 'latitude', 'longitude', 'is_location_exact', 'accommodates', 'bathrooms', 'bedrooms', 'beds', 'guests_included', 'extra_people', 'minimum_nights', 'maximum_nights', 'has_availability', 'availability_30', 'availability_60', 'availability_90', 'availability_365', 'number_of_reviews', 'number_of_reviews_ltm', 'review_scores_rating', 'review_scores_accuracy', 'review_scores_cleanliness', 'review_scores_checkin', 'review_scores_communication', 'review_scores_location', 'review_scores_value', 'requires_license', 'instant_bookable', 'is_business_travel_ready', 'require_guest_profile_picture', 'require_guest_phone_verification', 'calculated_host_listings_count', 'calculated_host_listings_count_entire_homes', 'calculated_host_listings_count_private_rooms', 'calculated_host_listings_count_shared_rooms', 'reviews_per_month']

    #preprocessing data with StandardScaler (numeric) and OneHotEncoder (categorical)
    preprocessor = ColumnTransformer(
    transformers=[
        ('scale', StandardScaler(), numeric_features),
        ('ohe', OneHotEncoder(handle_unknown= 'ignore'), categorical_features)
    ])

    #transforming data
    X_train = pd.DataFrame(preprocessor.fit_transform(X_train), index=X_train.index, columns = (numeric_features + list(preprocessor.named_transformers_['ohe'].get_feature_names(categorical_features))))

    X_test = pd.DataFrame(preprocessor.transform(X_test), index=X_test.index, columns=X_train.columns)

    #converting to csv

    ### The training and testing data live in the same directory as the processed datafile
    ### From the store_path, the closest parent directory is selected by splitting the store_path with "/"
    folder_dir = "/".join(store_path.split("/")[:-1])


    X_train.to_csv(folder_dir+"/" + "X_train.csv", index = False)
    y_train.to_csv(folder_dir+"/" + "y_train.csv", index = False, header = True)

    X_test.to_csv(folder_dir+"/" + "X_test.csv", index = False)
    y_test.to_csv(folder_dir+"/" + "y_test.csv", index = False, header = True)

    quebec_df.to_csv(store_path, index = False, header = True)

if __name__ == "__main__":
    main(opt["--quebec_path"], opt["--store_path"]) 
