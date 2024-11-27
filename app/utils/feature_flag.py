class FeatureFlagManager:
    def __init__(self, features_cfg):
        # Default configuration can come from environment variables
        self._features = features_cfg
    
    def is_enabled(self, feature_name):
        """Check if a feature is enabled."""
        return self._features.get(feature_name, False)
    
    def set_feature(self, feature_name, enabled):
        """Manually set a feature flag."""     
        self._features[feature_name] = enabled
    
    def enable_for_percentage(self, feature_name, percentage):
        """
        Enable feature for a percentage of users.
        Uses a simple hash-based distribution.
        """
        import hashlib
        
        def hash_user(user_id):
            return int(hashlib.md5(str(user_id).encode()).hexdigest(), 16)
        
        def is_feature_enabled_for_user(user_id):
            user_hash = hash_user(user_id)
            return (user_hash % 100) < percentage
        
        return is_feature_enabled_for_user

