"""UI theme and styling configuration."""

# Catppuccin Mocha color palette
class Theme:
    """Dark theme inspired by Catppuccin Mocha."""

    # Main colors
    BG_PRIMARY = "#1E1E2E"        # Dark background
    BG_SECONDARY = "#313244"      # Secondary background
    BG_TERTIARY = "#45475A"       # Tertiary background
    FG_PRIMARY = "#CDD6F4"        # Main text
    FG_SECONDARY = "#BAC2DE"      # Secondary text
    FG_MUTED = "#6C7086"          # Muted text

    # Accent colors
    ACCENT_BLUE = "#89B4FA"       # Primary accent
    ACCENT_GREEN = "#A6E3A1"      # Success/Terminal
    ACCENT_RED = "#F38BA8"        # Error
    ACCENT_YELLOW = "#F9E2AF"     # Warning
    ACCENT_TEAL = "#94E2D5"       # Info

    # Semantic colors
    SUCCESS = ACCENT_GREEN
    ERROR = ACCENT_RED
    WARNING = ACCENT_YELLOW
    INFO = ACCENT_TEAL

    # UI Component Colors
    BUTTON_BG = ACCENT_BLUE
    BUTTON_FG = "#11111B"         # Almost black
    BUTTON_HOVER = "#B4BEFE"      # Lighter blue
    BUTTON_ACTIVE = "#7AA2F7"     # Darker blue

    INPUT_BG = BG_SECONDARY
    INPUT_FG = FG_PRIMARY
    INPUT_BORDER = BG_TERTIARY

    TERMINAL_BG = "#11111B"       # Almost black
    TERMINAL_FG = SUCCESS


# Font configurations
class Fonts:
    """Font settings for different UI elements."""

    TITLE = ("Segoe UI", 24, "bold")
    HEADING = ("Segoe UI", 12, "bold")
    LABEL = ("Segoe UI", 10)
    LABEL_BOLD = ("Segoe UI", 10, "bold")
    BUTTON = ("Segoe UI", 11, "bold")
    INPUT = ("Segoe UI", 11)
    TERMINAL = ("Consolas", 10)
    SMALL = ("Segoe UI", 8, "italic")


# Spacing and dimensions
class Spacing:
    """Spacing and sizing constants."""

    PADDING_LARGE = 20
    PADDING_MEDIUM = 15
    PADDING_SMALL = 10
    PADDING_TINY = 5

    BORDER_RADIUS = 4
    BUTTON_HEIGHT = 40
    INPUT_HEIGHT = 32
