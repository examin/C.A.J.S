
import logging
def outputAs(name,df):
    try:
        df.to_csv('Output/'+name+'.csv')
        logging.info(name+" Data Updated")
        return True
    except Exception as e:
        logging.info(name+" Data unable to Updated due to "+str(e))
        return False
def outputAsCve(name,df):
    try:
        df.to_csv(name+'.csv')
        logging.info(name+" Data Updated")
        return True
    except Exception as e:
        logging.info(name+" Data unable to Updated due to "+str(e))
        return False
def outputAsJson(name,df):
     try:
          df.to_json(name+'.json', orient='records')
          return True
     except Exception as e:
        logging.info(name+" Data unable to Updated due to "+str(e))
        return False
def outputAsExcel(name,df):
     try:
         writer = ExcelWriter("Output/Tomcat_8" +".xlsx")
         logging.info(name+" Data Updated")
         df.to_excel(writer, 'CVE Details', index=False)
         writer.save()
         return True
     except Exception as e:
        logging.info(name+" Data unable to Updated due to "+str(e))
        return False
