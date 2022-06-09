import win32com.client
import pywintypes
import datetime
import os
from dateutil.relativedelta import relativedelta
from icalendar import Calendar, Event, vCalAddress, vText

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

calendar = outlook.GetDefaultFolder(9)

items = calendar.Items # このitemsが一つ一つの「予定」


select_items = [] # 指定した期間内の予定を入れるリスト

# 予定を抜き出したい期間を指定
start_date = datetime.date.today() - relativedelta(months=1)
end_date = datetime.date.today() + relativedelta(months=3)

for item in items:
    if start_date <= item.start.date() <= end_date:
        select_items.append(item)

# 抜き出した予定の詳細を表示
if False:
    for select_item in select_items:
        print("Actions: ", select_item.actions)
        print("AllDayEvent: ", select_item.alldayevent)
        print("Application: ", select_item.application)
        print("Attachments: ", select_item.attachments)
        print("AutoResolvedWinner: ", select_item.autoresolvedwinner)
        print("BillingInformation: ", select_item.billinginformation)
        # print("Body: ", select_item.
        print("BusyStatus: ", select_item.busystatus)
        print("Categories: ", select_item.categories)
        print("Class: ", select_item.Class)
        print("Companies: ", select_item.companies)
        print("Conflicts: ", select_item.conflicts)
        print("ConversationID: ", select_item.conversationid)
        print("ConversationIndex: ", select_item.conversationindex)
        print("ConversationTopic: ", select_item.conversationtopic)
        print("CreationTime: ", select_item.creationtime)
        print("DownloadState: ", select_item.downloadstate)
        print("Duration: ", select_item.duration)
        print("End: ", select_item.end)
        print("EndInEndTimeZone: ", select_item.endinendtimezone)
        print("EndTimeZone: ", select_item.endtimezone)
        print("EndUTC: ", select_item.endutc)
        print("EntryID: ", select_item.entryid)
        print("ForceUpdateToAllAttendees: ", select_item.forceupdatetoallattendees)
        print("FormDescription: ", select_item.formdescription)
        print("GetInspector: ", select_item.getinspector)
        print("GlobalAppointmentID: ", select_item.globalappointmentid)
        print("Importance: ", select_item.importance)
        print("InternetCodepage: ", select_item.internetcodepage)
        print("IsConflict: ", select_item.isconflict)
        print("IsRecurring: ", select_item.isrecurring)
        print("ItemProperties: ", select_item.itemproperties)
        print("LastModificationTime: ", select_item.lastmodificationtime)
        print("Location: ", select_item.location)
        print("MarkForDownload: ", select_item.markfordownload)
        print("MeetingStatus: ", select_item.meetingstatus)
        print("MeetingWorkspaceURL: ", select_item.meetingworkspaceurl)
        print("MessageClass: ", select_item.messageclass)
        print("Mileage: ", select_item.mileage)
        print("NoAging: ", select_item.noaging)
        print("OptionalAttendees: ", select_item.optionalattendees)
        print("Organizer: ", select_item.organizer)
        print("OutlookInternalVersion: ", select_item.outlookinternalversion)
        print("OutlookVersion: ", select_item.outlookversion)
        print("Parent: ", select_item.parent)
        print("PropertyAccessor: ", select_item.propertyaccessor)
        print("Recipients: ", select_item.recipients)
        print("RecurrenceState: ", select_item.recurrencestate)
        print("ReminderMinutesBeforeStart: ", select_item.reminderminutesbeforestart)
        print("ReminderOverrideDefault: ", select_item.reminderoverridedefault)
        print("ReminderPlaySound: ", select_item.reminderplaysound)
        print("ReminderSet: ", select_item.reminderset)
        print("ReminderSoundFile: ", select_item.remindersoundfile)
        print("ReplyTime: ", select_item.replytime)
        print("RequiredAttendees: ", select_item.requiredattendees)
        print("Resources: ", select_item.resources)
        print("ResponseRequested: ", select_item.responserequested)
        print("ResponseStatus: ", select_item.responsestatus)
        print("RTFBody: ", select_item.rtfbody)
        print("Saved: ", select_item.saved)
        print("SendUsingAccount: ", select_item.sendusingaccount)
        print("Sensitivity: ", select_item.sensitivity)
        print("Session: ", select_item.session)
        print("Size: ", select_item.size)
        print("Start: ", select_item.start)
        print("StartInStartTimeZone: ", select_item.startinstarttimezone)
        print("StartTimeZone: ", select_item.starttimezone)
        print("StartUTC: ", select_item.startutc)
        print("Subject: ", select_item.subject)
        print("UnRead: ", select_item.unread)
        print("UserProperties: ", select_item.userproperties)
        print("----")

calExp = calendar.GetCalendarExporter()

# Set export parameters
calExp.StartDate = pywintypes.Time(start_date)
calExp.EndDate = pywintypes.Time(end_date)
calExp.IncludeAttachments = False
calExp.IncludePrivateDetails = True
calExp.CalendarDetail = 2 # https://docs.microsoft.com/ja-jp/office/vba/api/outlook.olcalendardetail 1 = FreeBusyAndSubject, 2 = FullDetails, 0 = olFreeBusyOnly
calExp.SaveAsICal(os.getcwd() + "./sample.ics")

print(calExp.StartDate)
print(calExp.EndDate)

# Read ical files
if True:
    e = open(os.getcwd() + "./sample.ics", 'rb')
    ecal = Calendar.from_ical(e.read())
    for component in ecal.walk():
        if component.name == "VTIMEZONE":
            print("TZID: ", component.get("TZID"))
            for var in component.walk():
                if var.name == "STANDARD":
                    print("TZOFFSETTO: ", abs(var.decoded("tzoffsetto")))
                    print("TZOFFSETFROM: ", var.decoded("tzoffsetfrom"))

        if component.name == "VEVENT":
            #print(component.property_items()) # print available properties
            if False:
                print("summary: ", component.get("summary"))
                #print("desc: ", component.get("description"))
                print("class: ", component.get("class"))
                print("transp: ", component.get("transp"))
                print("rrule: ", component.get("RRULE"))
                print("start: ", component.decoded("dtstart"))
                print("end: ", component.decoded("dtend"))
                print("location: ", component.get("location"))
    e.close()