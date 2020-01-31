"""
Usage:
    eda_summary.py [--data_dir=<data_dir>] [--file_dir=<file_dir>]
    eda_summary.py -h | --help


Options:
-h --help                         show this screen
-d --data_dir=<data_dir>          directory of the folder that has data [default: data/cleaned_data.csv]
-f --file_dir=<file_dir>          directory of the folder to save generated images/tables [default: eda/]
"""


# import library, package
import altair as alt
import pandas as pd
import numpy as np
from docopt import docopt

def main():
    arguments = docopt(__doc__)
    print(arguments)

    # Define data directory
    data_dir = arguments["--data_dir"]

    # Define file directory
    file_dir = arguments["--file_dir"]
    if file_dir.endswith("/") == False:
        file_dir = file_dir+"/"

    eda = EDA(data_dir, file_dir)
    eda.summarize()
    eda.corr_table()
    eda.corr_plots()

    message = "Successfully Executed"

    return message


class EDA():

    def __init__(self, data_dir, file_dir):

        """
        Create a class for EDA

        :param:
        -------
        data_dir : str    -- path to your .csv file
        file_dir : str    -- path to save your generated data

        """
        # assign attributes to the class

        self.data_dir = data_dir
        self.file_dir = file_dir

        data = pd.read_csv(data_dir)
        self.data = data

    def summarize(self):
        """
        Summarize the data and provide descriptive statistics

        :param:
        - self

        :return:
        - pd.DataFrame  -- DataFrame that consists of information about data
        :example:
        > a = EDA("~/Desktop/data_file.csv")
        > a.summarize()
        """

        columns = self.data.columns
        summary = self.data[columns].describe(include="all")
        summary.to_csv(self.file_dir+"descriptive_statistics.csv")
        return summary


    def corr_table(self, metric="pearson"):
        """
        Create Correlation table between two variables

        :param:
        - metric : str       -- specify how to calculate correlation
                                options:("pearson","spearman","kendall","callable")
        :returns:
        - pd.DataFrame   -- DataFrame that consists of information about correlation between stated variables

        :example:
        > a = EDA("~/Desktop/data_file.csv")
        > a.corr_table()
        """
        columns = self.data.columns
        correlation_table = self.data[columns].corr(method=metric)
        correlation_table.to_csv(self.file_dir+"corr_table.csv")

        return correlation_table


    def corr_plots(self):
        """
        Create Correlation plots of variables

        :returns:
        - altair.obj   -- DataFrame that consists of information about correlation between stated variables

        :example:
        > a = EDA("~/Desktop/data_file.csv")
        > a.corr_plots
        """

        categorical_features = ['host_response_time', 'property_type', 'room_type', 'bed_type']
        numeric_features = ['host_response_rate', 'host_is_superhost', 'host_listings_count', 'host_has_profile_pic',
                            'host_identity_verified', 'latitude', 'longitude', 'is_location_exact', 'accommodates',
                            'bathrooms', 'bedrooms', 'beds', 'guests_included', 'extra_people', 'minimum_nights',
                            'maximum_nights', 'has_availability', 'availability_30', 'availability_60',
                            'availability_90', 'availability_365', 'number_of_reviews', 'number_of_reviews_ltm',
                            'review_scores_rating', 'review_scores_accuracy', 'review_scores_cleanliness',
                            'review_scores_checkin', 'review_scores_communication', 'review_scores_location',
                            'review_scores_value', 'requires_license', 'instant_bookable', 'is_business_travel_ready',
                            'require_guest_profile_picture', 'require_guest_phone_verification',
                            'calculated_host_listings_count', 'calculated_host_listings_count_entire_homes',
                            'calculated_host_listings_count_private_rooms',
                            'calculated_host_listings_count_shared_rooms', 'reviews_per_month']

        # Specify response & predictor
        response = "price"

        # Seperate list for categorical & numerical features
        num_index = list(range(len(numeric_features)))
        group_num_index = np.array_split(num_index, 5)
        num_groups = [[numeric_features[i] for i in x] for x in group_num_index]

        i = 0

        # Price vs Categorical Plots

        plot = alt.Chart(self.data).mark_circle().encode(
                                              alt.X(alt.repeat("column"), type="nominal"),
                                              alt.Y(alt.repeat("row"), type="quantitative")
        ).properties(
        width=150,
        height=150
        ).repeat(
        row = [response],
        column = categorical_features
        ).interactive()

        # save plot

        plot.save(self.file_dir+"response_categorical_correlation_plot.html".format(i))
        print("Plot saved")

        i = 0
        # Numerical Plots
        for predictor_group in num_groups:
            plot = alt.Chart(self.data).mark_circle().encode(
                                                  alt.X(alt.repeat("column"), type="quantitative"),
                                                  alt.Y(alt.repeat("row"), type="quantitative")
            ).properties(
            width=150,
            height=150
            ).repeat(
            row = [response] + predictor_group,
            column = [response] + predictor_group
            ).interactive()

            # save plot

            i += 1
            plot.save(self.file_dir+"response_numerical_correlation_plot{}.html".format(i))
            print("Plot saved")

if __name__ == '__main__':
    main()