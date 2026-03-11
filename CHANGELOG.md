# SN-HMSTR CHANGELOG

## v1.1.9 - Engine API Integration

### Added
- Real Hamster API client
- Tap request endpoint
- Tasks auto-check module
- Promo reward detection

### Changed
- Engine now communicates with real server
- Removed placeholder API system

### Fixed
- Tap farming loop previously simulated

## v1.1.7
Fix:
- run_tap() missing account argument
- engine now passes account object to modules
- stabilize multi-account execution

Updated Files:
- core/engine.py
