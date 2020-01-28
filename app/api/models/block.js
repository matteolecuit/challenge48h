const Device = Device {
    index: {
        type: Number,
        require: true
    },
    timestamp: {
        type: Date,
        require: true
    },
    data : {
        type: String,
        require: true
    },
    contributor_id: {
        type: String,
        require: true
    },
    previous_hash: {
        type: String,
        require: true
    },
    nonce: {
        type: Number,
        require: true
    },
    difficulty: {
        type: Number,
        require: true
    },
    hash: {
        type: String,
        require: true
    }
    
    
});
