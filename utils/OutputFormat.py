
import logging

from pandas import ExcelWriter


def outputAs(name, df):
    try:
        df.to_csv('Output/' + name + '.csv')
        logging.info(name + " Data Updated ")
        return True
    except Exception as e:
        logging.info(name + " Data unable to Updated due to " + str(e))
        return False


def outputAsCve(name, df):
    try:
        df.to_csv(name + '.csv')
        print(" Output successfully written  as " +
              additional_output_as + "for " + name)
        return True
    except Exception as e:
        logging.info(name + " Data unable to Updated due to " + str(e))
        return False


def outputAsJson(name, df):
    try:
        df.to_json(name + '.json', orient='records')
        print(" Output successfully written  as " +
              additional_output_as + "for " + name)
        return True
    except Exception as e:
        logging.info(name + " Data unable to Updated due to " + str(e))
        return False


def outputAsExcel(name, df):
    try:
        writer = ExcelWriter("Output/" + "name" + ".xlsx")
        df.to_excel(writer, 'CVE Details', index=False)
        writer.save()
        print(" Output successfully written  as " +
              additional_output_as + "for " + name)
        return True
    except Exception as e:
        logging.info(name + " Data unable to Updated due to " + str(e))
        return False


def custom_output(additional_output_as, name, df):
    if additional_output_as == 'json':
        is_written = outputAsJson(name, df)
    if additional_output_as == 'csv':
        is_written = outputAsExcel(name, df)
