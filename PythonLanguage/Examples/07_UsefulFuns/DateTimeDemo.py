from datetime import date, timezone
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta


# 取得現在或指定日期時間，以及比較2個日期大小
def datetimeDemo():
    # 指定UTC時區，也就是0度經線的時間
    epoch = datetime(1970, 1, 1, tzinfo=timezone.utc)
    # 可以將指定日期時間轉成時間戳記 ("秒.微秒" 型式)
    print(f"epoch: {epoch}; timestamp: {datetime.timestamp(epoch)}")
    # 取得現在日期時間
    now = datetime.now()
    print(f"now: {now}")
    # 取得年、月、日、時、分、秒
    print(f"now.year: {now.year}")
    print(f"now.month: {now.month}")
    print(f"now.day: {now.day}")
    print(f"now.weekday(): {now.weekday()}")  # Monday == 0 ... Sunday == 6.
    print(f"now.hour: {now.hour}")
    print(f"now.minute: {now.minute}")
    print(f"now.second: {now.second}")
    # 指定日期時間
    myBirthday = datetime(year=2000, month=1, day=1, hour=23)
    print(f"my birthday: {myBirthday}")
    # 日期時間比較
    print(f"now is after My birthday? {now > myBirthday}")


# 取得現在或指定日期
def dateDemo():
    # 取得現在日期
    today = date.today()
    print(f"today: {today}")
    # 指定日期
    myBirthday = date(year=2000, month=1, day=1)
    print(f"my birthday: {myBirthday}")


# 加減指定單位時間
def timedeltaDemo():
    now = datetime.now()
    myBirthday = datetime(year=2000, month=1, day=1, hour=23)
    # 日期時間加減指定單位時間(不包含年、月)
    print(f"now + timedelta(days=1): {now + timedelta(days=1)}")
    print(f"now - timedelta(days=1): {now - timedelta(days=1)}")
    tDelta = now - myBirthday
    print(f"now - myBirthday: {tDelta.days} days")
    # 要加減年、月必須額外安裝python-dateutil
    rDelta_1y_1m = relativedelta(years=1, months=1)
    print(f"now + rDelta_1y_1m: {now + rDelta_1y_1m}")
    print(f"now - rDelta_1y_1m: {now - rDelta_1y_1m}")
    rDelta = relativedelta(dt1=now, dt2=myBirthday)
    print(
        f"my age: {rDelta.years} years, {rDelta.months} months, {rDelta.days} days")


def formatParseDemo():
    # 日期時間格式符號，參看 https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

    now = datetime.now()

    # 使用datetime.strftime()格式化日期時間
    fmt = "%Y/%m/%d %H:%M:%S"
    print(f"{now} is formatted to '{now.strftime(fmt)}'")

    # 使用str.format()格式化日期時間
    # ":"前面為index，可省略代表依序指定後面提供的值
    # "%B"-月份完整名稱；"%A"-星期幾；"%I"-時(12時制)；"%M"-分；"%p"-AM或PM
    print("str.format(): {:%B-%d-%y %A %I:%M%p}".format(now))

    # 將文字類型的日期時間解析回datetime物件
    datetimeStr = "2000/1/1 23:0:0"
    datetimeParsed = datetime.strptime(datetimeStr, fmt)
    print(f"'{datetimeStr}' is parsed to {datetimeParsed}")


def timezoneDemo():
    # 取得現在日期時間(當地時區)
    now_local = datetime.now()
    print(f"now_local: {now_local}")
    # 取得帶有時區的日期時間
    print(f"now_local.astimezone(): {now_local.astimezone()}")

    # 下列2種都可取得現在日期時間(UTC時區)
    now_utc = datetime.now(timezone.utc)
    # 已經列為deprecated，不建議使用
    # now_utc = datetime.utcnow()
    print(f"now_utc: {now_utc}")

    # 取得現在日期時間(+8時區)
    now_8h = datetime.now(timezone(offset=timedelta(hours=8)))
    print(f"now_8h: {now_8h}")

    # 指定日期時間(當地時區)
    dt_local = datetime(2000, 1, 1, 23)
    print(f"dt_local: {dt_local.astimezone()}")

    # 指定日期時間(UTC時區)
    dt_utc = datetime(2000, 1, 1, 23, tzinfo=timezone.utc)
    print(f"dt_utc: {dt_utc}")

    # 指定日期時間(+8時區)
    dt_8h = datetime(2000, 1, 1, 23, tzinfo=timezone(
        offset=timedelta(hours=8)))
    print(f"dt_8h: {dt_8h}")


def main():
    datetimeDemo()
    print("---------------------------------------")
    dateDemo()
    print("---------------------------------------")
    timedeltaDemo()
    print("---------------------------------------")
    formatParseDemo()
    print("---------------------------------------")
    timezoneDemo()


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
