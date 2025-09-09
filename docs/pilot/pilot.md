# Simple CV Attendance & Invigilation System

```
attendance_system/
├── README.md
├── requirements.txt
├── config.yaml
├── .env
│
├── models/
│   ├── __init__.py
│   ├── yolo_detector.py          # YOLO detection
│   ├── face_recognizer.py        # Face detection + recognition
│   ├── tracker.py                # DeepSORT tracking
│   └── behavior_analyzer.py      # Suspicious behavior detection
│
├── database/
│   ├── __init__.py
│   ├── mongo_handler.py          # MongoDB operations
│   └── schemas.py                # Data models/schemas
│
├── utils/
│   ├── __init__.py
│   ├── video_utils.py            # Video processing utilities
│   ├── image_utils.py            # Image preprocessing
│   └── alert_utils.py            # Alert generation
│
├── core/
│   ├── __init__.py
│   ├── pipeline.py               # Main processing pipeline
│   ├── attendance_manager.py     # Attendance tracking logic
│   └── alert_system.py           # Alert management
│
├── data/
│   ├── face_gallery/             # Student face images
│   ├── models/                   # Saved model weights
│   │   ├── yolov8.pt
│   │   ├── face_model.onnx
│   │   └── reid_model.pt
│   └── evidence/                 # Alert screenshots/videos
│
├── scripts/
│   ├── train_models.py           # Model training
│   ├── setup_database.py         # Database initialization
│   └── run_system.py             # Main execution script
│
└── tests/
    ├── test_models.py
    ├── test_database.py
    └── test_pipeline.py
```

## Key Files Breakdown:

### Core Components (4 main files):
1. *models/yolo_detector.py* - Person/object detection using YOLO
2. *models/face_recognizer.py* - Face detection and recognition pipeline  
3. *models/tracker.py* - Multi-object tracking with DeepSORT
4. *models/behavior_analyzer.py* - Detect cheating/suspicious behaviors

### Database (2 files):
1. *database/mongo_handler.py* - All MongoDB operations
2. *database/schemas.py* - Data structures for students, sessions, alerts

### Processing Pipeline (3 files):
1. *core/pipeline.py* - Main video processing loop
2. *core/attendance_manager.py* - Handle entry/exit, attendance logging
3. *core/alert_system.py* - Generate and manage alerts

### Utilities (3 helper files):
1. *utils/video_utils.py* - Video reading, frame processing
2. *utils/image_utils.py* - Image preprocessing, enhancement
3. *utils/alert_utils.py* - Alert formatting, evidence capture

This structure gives you everything you need while keeping it manageable - just 15 core Python files to implement your entire system!

### System Requirements
- **CPU**: 4+ cores recommended for face recognition
- **RAM**: 8GB+ (depends on image batch size)
- **Storage**: 10GB+ (for images, models, and database)
- **OS**: Ubuntu 20.04+, Windows 10+, macOS 11+