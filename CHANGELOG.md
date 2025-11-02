# Changelog

## [1.0.3] - 2023-11-23

### Added
- Implemented drag-and-drop reordering for the layers panel, allowing for intuitive control over layer z-index. The default background layer remains fixed at the bottom.

### Removed
- Removed the up and down arrow buttons from the layers panel, as they are now redundant.

## [1.0.2] - 2023-11-22

### Fixed
- The canvas content area now correctly resizes along with the canvas itself, preventing content from being clipped when switching to the 1200x1200px size.
- Improved the reliability and performance of the drag-and-drop functionality by optimizing the event handling process.

### Changed
- Renamed the "Current" canvas size option in the dropdown menu to "1200x720" for better clarity.

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
