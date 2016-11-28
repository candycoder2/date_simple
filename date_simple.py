import datetime as dt


def get_date(string=dt.date.today().strftime('%Y-%m-%d')): # (produce a datetime.date object based on a string)
    dateformatlist = ['%Y-%m-%d', '%d-%B-%y', '%m/%d/%Y']

    if isinstance(string, str):
      for dateformat in dateformatlist:
        try:
          return dt.datetime.strptime(string, dateformat)
        except ValueError:
          continue
    raise Exception("get_date() : Error with the input, date provided does not match any of date formats " ) #+ str(dateformatlist))


def add_day(datet, days1 = 1):
        try:
            day_advanced = datet + dt.timedelta(days=days1)
            return day_advanced
        except TypeError, e:
            raise TypeError("Error with the input in add_day {}".format(e))

def add_week(datet, weeks1 = 1):
        try:
            return datet + dt.timedelta(weeks = weeks1)
        except TypeError, e:
            raise TypeError("Error with the input in add_week{}".format(e))

def format_date(datet,format="%m/%d/%Y"):
    try:
        return dt.datetime.strftime(datet, format)
    except ValueError, e:
        raise ValueError("the date needs to be corrected{}".format(e))

def month_only(datet):
    try:
        return dt.datetime.strftime(datet, "%m")
    except TypeError, e:
        raise TypeError("Error with the input with getting the month only{}".format(e))

def main ():
    datet = get_date()
    add_day(datet, days1 = 1)
    add_week(datet, weeks1 = 1)
    format_date(datet)
    month_only(datet)



if __name__ == '__main__':
    main()

    print add_week(dt.datetime(2016, 5, 5, 0, 0), 1)
    print add_week(dt.datetime(2016, 5, 5, 0, 0), 2)
    print ""
    print format_date(dt.datetime(2016, 5, 5, 0, 0))
    print format_date(dt.datetime(2016, 5, 6, 0, 0))

    print format_date(dt.datetime(2016, 7, 5, 0, 0))
