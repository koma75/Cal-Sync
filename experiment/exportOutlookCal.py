import win32com.client
import pywintypes
import datetime
import os
from dateutil.relativedelta import relativedelta
from icalendar import Calendar, Event, vCalAddress, vText

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

calendar = outlook.GetDefaultFolder(9)

# 予定を抜き出したい期間を指定
start_date = datetime.date.today() - relativedelta(months=6)
end_date = datetime.date.today() + relativedelta(months=3)

calExp = calendar.GetCalendarExporter()

# Set export parameters
calExp.StartDate = pywintypes.Time(start_date)
calExp.EndDate = pywintypes.Time(end_date)
calExp.IncludeAttachments = False
calExp.IncludePrivateDetails = True
calExp.CalendarDetail = 1 # https://docs.microsoft.com/ja-jp/office/vba/api/outlook.olcalendardetail 1 = FreeBusyAndSubject, 2 = FullDetails, 0 = olFreeBusyOnly
calExp.SaveAsICal(os.getcwd() + "./output.ics")