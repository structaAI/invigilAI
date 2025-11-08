import logging
import json
from datetime import datetime
from pathlib import Path
from typing import Dict

class SystemLogger:
  def __init__(self, log_dir: str = "outputs/logs"):
    self.log_dir = Path(log_dir)
    self.log_dir.mkdir(exist_ok=True)
    
    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(self.log_dir / 'system.log'),
            logging.StreamHandler()
        ]
    )
    self.logger = logging.getLogger(__name__)
  
  def log_attendance(self, attendance_data: Dict):
    """Log attendance changes"""
    self.logger.info(f"Attendance - {attendance_data['student_id']} - {attendance_data['status']}")
  
  def log_violation(self, violation_data: Dict):
    """Log violation detection"""
    self.logger.warning(f"Violation - {violation_data['class_name']} - Confidence: {violation_data['confidence']:.2f}")
  
  def log_system(self, message: str):
    """Log system messages"""
    self.logger.info(message)
  
  def log_error(self, message: str):
    """Log error messages"""
    self.logger.error(message)