def count_ids_in_events(members, events):
    mention_count = {member: 0 for member in members}  # Initialize counts for each member
    active_users = set(members)  # Track currently active users
    user_offline_until = {}  # Track when users will come back online

    # Loop through events
    for event in events:
        event_type = event[0]
        timestamp = int(event[1])

        print(f"\nProcessing event: {event}")
        print(f"Active users before event: {active_users}")

        if event_type == 'MESSAGE':
            # Add users back to active_users if their offline time has expired
            for user in list(user_offline_until.keys()):
                if user_offline_until[user] <= timestamp and user not in active_users:
                    active_users.add(user)
                    print(f"{user} has come back online and is added to active users.")

            mentions = event[2].strip().split()  # Split the mentions in the message
            unique_mentions = set()  # Set to track unique mentions

            # Handle mentions
            if 'ALL' in mentions:
                unique_mentions.update(members)
            if 'HERE' in mentions:
                unique_mentions.update(active_users)

            # Add specific members mentioned in the message
            unique_mentions.update(m for m in mentions if m.startswith('id') and m in members)

            print(f"Unique mentions identified: {unique_mentions}")

            for member in unique_mentions:
                mention_count[member] += 1
                print(f"Incremented mention count for {member}: {mention_count[member]}")

        elif event_type == 'OFFLINE':
            user_id = event[2]
            user_offline_until[user_id] = timestamp + 60
            print(f"{user_id} is now offline until timestamp {user_offline_until[user_id]}")

        # Remove from active users until time is up
        for user in list(active_users):
            if user in user_offline_until and user_offline_until[user] >= timestamp:
                active_users.remove(user)
                print(f"{user} has gone offline and is removed from active users.")

        print(f"Active users after event: {active_users}")

    result = [f'{member}={mention_count[member]}' for member in sorted(members)]
    return result


member_ids = ["id42", "id158", "id23"]
event_list = [
    ["MESSAGE", "0", "ALL id158 id42"],
    ["OFFLINE", "1", "id158"],
    ["MESSAGE", "2", "id158 id158"],
    ["OFFLINE", "3", "id23"],
    ["MESSAGE", "60", "HERE id158 id42 id23"],
    ["MESSAGE", "61", "HERE"]
]

output = count_ids_in_events(member_ids, event_list)
print("Final output:", output)  # Expected output: ["id158=4", "id23=2", "id42=3"]
