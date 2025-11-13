from datetime import datetime, timedelta

def evening_schedule():
    print("🌇 Evening Routine Planner 🌙")
    print(f"Current time: {datetime.now().strftime('%I:%M %p')}\n")

    # Tasks and their estimated durations (in minutes)
    tasks = [
        ("Go get groceries", 60),
        ("Make dinner", 45),
        ("Feed the kids", 20),
        ("Feed the dog", 5),
        ("Walk the dog", 20),
        ("Shower", 15),
        ("Put the kids to sleep", 20),
        ("Go to bed", 0)
    ]

    start_time = datetime.now().replace(hour=16, minute=0, second=0, microsecond=0)
    current_time = start_time

    print("Here's your plan for the evening:\n")
    for i, (task, duration) in enumerate(tasks, 1):
        end_time = current_time + timedelta(minutes=duration)
        print(f"{i}. {task} — {current_time.strftime('%I:%M %p')} to {end_time.strftime('%I:%M %p')}")
        current_time = end_time

    print("\nLet's go through your tasks! Type 'done' when you finish each one.\n")

    for i, (task, _) in enumerate(tasks, 1):
        input(f"→ {task} — press Enter when done: ")
        print(f"✅ Task {i}: {task} completed!\n")

    print("🎉 All tasks done! Time to rest — good night! 😴")

if __name__ == "__main__":
    evening_schedule()
