import logging

logging.basicConfig(format='%(asctime)s %(message)s', datefmt ='%m/%d/%Y %I:%M:%S %p', filename ='pythonoutput.log' , level =logging.INFO)

logging.warning("Fruits found!")
fruits =["apple","banana","grapes"]

for f in fruits:
    logging.info("found Fruits %s" %f)

    logging.debug("job's done")