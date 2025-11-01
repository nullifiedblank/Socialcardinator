# Changelog

## [1.0.1] - 2023-11-21

### Fixed
- The "Current" canvas size option now correctly reverts to the initial canvas dimensions instead of being hardcoded.
- The content of the floating preview panel is now non-interactable, preventing accidental clicks on its elements.

### Changed
- The X and Y position input fields in the control panel now update in real-time as an element is dragged on the canvas.

## [1.0.0] - 2023-11-20

### Initial Features
- Add canvas resizing dropdown with options for current size, 1200x1200, and custom dimensions.
- Implement a floating preview panel that displays a scaled-down version of the main canvas.
- Introduce zoom-on-scroll functionality for the main canvas, allowing users to zoom in and out using the mouse wheel while holding the Ctrl key.
- Implement Canva-style drag-and-drop for elements on the main canvas.
