def study_schedule(start_time, end_time, target_time):
    if (not start_time or not target_time):
        return 0

    result = 0
    countStudents = len(start_time)
    for i in range(0, countStudents):
        if (target_time >= start_time[i] and target_time <= end_time[i]):
            result += 1

    return result
