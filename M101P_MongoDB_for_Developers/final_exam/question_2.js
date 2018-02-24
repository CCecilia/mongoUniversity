db.messages.aggregate([
    {
        $unwind: "$headers.To"
    },
    {
        $group: 
            {
                _id: {
                    sender: "$headers.From",
                    receipient:"$headers.To"
                },
                total_msgs: { $sum: 1 }
            }
    },
    {
        $sort: {total_msgs: -1}
    }
]);