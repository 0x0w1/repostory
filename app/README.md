# Repository Dashboard

A React-based dashboard for visualizing Git repository stars and forks trends from the `repo_data` directory.

## Features

- 📊 Interactive charts using Recharts
- 🎯 Repository selection (up to 5 repositories)
- 📈 Stars and forks metrics comparison
- 📱 Responsive design with Tailwind CSS
- 🔄 Real-time data loading from JSON files

## Technology Stack

- **Framework**: React 18 (CSR)
- **Build Tool**: Vite
- **Styling**: Tailwind CSS
- **Charts**: Recharts
- **Language**: JavaScript (ES6+)

## Getting Started

### Prerequisites

- Node.js 16+ or UV package manager

### Installation

```bash
# Install dependencies
npm install
# or if using UV
uv sync
```

### Development

```bash
# Start development server
npm run dev
# or
uv run npm run dev
```

The application will be available at `http://localhost:3000`

### Build

```bash
# Build for production
npm run build
# or
uv run npm run build
```

### Preview

```bash
# Preview production build
npm run preview
# or
uv run npm run preview
```

## Configuration

### Data Source Path

You can configure the data source path using environment variables:

- Create a `.env` file in the app directory
- Set `VITE_DATA_SOURCE_PATH` to your desired path (default: `../repo_data`)

Example:
```env
VITE_DATA_SOURCE_PATH=../repo_data
```

## Data Format

The application expects JSON files in the following format:

```json
{
  "total_stars": 84386,
  "fetched_at": "2025-07-29T17:14:42.677309",
  "stars_by_date": {
    "2012-04-28": 3772,
    "2012-04-29": 4
  },
  "forks_by_date": {
    "2012-04-28": 145,
    "2012-04-29": 2
  }
}
```

## Usage

1. **Select Metric**: Choose between Stars or Forks to visualize
2. **Select Repositories**: Choose up to 5 repositories to compare
3. **View Charts**: Interactive line charts show trends over time
4. **Repository Stats**: View summary statistics for selected repositories

## Features

### Interactive Charts
- Line charts with hover tooltips
- Responsive design that adapts to screen size
- Custom formatting for large numbers (K, M)
- Time-based X-axis with yearly labels

### Repository Selection
- Checkbox-based selection interface
- Maximum 5 repositories for optimal visualization
- Real-time star count display
- Easy removal of selected repositories

### Responsive Design
- Mobile-first approach
- Grid-based layout that adapts to screen size
- Optimized for both desktop and mobile viewing

## Development

### Project Structure

```
app/
├── src/
│   ├── components/
│   │   ├── Dashboard.jsx     # Main dashboard component
│   │   ├── Chart.jsx         # Chart visualization component
│   │   ├── RepositorySelector.jsx # Repository selection component
│   │   └── MetricSelector.jsx     # Metric selection component
│   ├── utils/
│   │   └── dataLoader.js     # Data loading and processing utilities
│   ├── index.css            # Tailwind CSS imports and custom styles
│   └── main.jsx             # Application entry point
├── public/                  # Static assets
├── package.json            # Dependencies and scripts
├── vite.config.js          # Vite configuration
├── tailwind.config.js      # Tailwind CSS configuration
└── README.md              # This file
```

### Key Components

- **Dashboard**: Main application component managing state and layout
- **Chart**: Recharts-based line chart with custom styling
- **RepositorySelector**: Multi-select interface for repositories
- **MetricSelector**: Toggle between stars and forks metrics
- **DataLoader**: Utilities for loading and processing JSON data

## Troubleshooting

### Data Loading Issues

If data is not loading:
1. Ensure the `repo_data` directory exists and contains JSON files
2. Check that JSON files follow the expected format
3. Verify the data source path in environment variables
4. Check browser console for network or parsing errors

### Build Issues

If the build fails:
1. Ensure all dependencies are installed
2. Check that all import paths are correct
3. Verify that environment variables are properly set
4. Clear node_modules and reinstall if needed