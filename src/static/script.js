// Configuration
const API_URL = 'http://localhost/ph-latest?limit=20'; // Replace with your API endpoint
const REFRESH_INTERVAL = 1000; // Refresh every 5 seconds

// ApexCharts Configuration
const chartOptions = {
  chart: {
    type: 'line', // Chart type: line, bar, pie, etc.
    height: 350,
    animations: {
      enabled: true,
      easing: 'linear',
      dynamicAnimation: {
        speed: 1000, // Animation speed
      },
    },
  },
  series: [{
    name: 'Data Series',
    data: [], // Initial empty data
  }],
  xaxis: {
    categories: [], // Initial empty categories for the x-axis
  },
  title: {
    text: 'Real-Time Data Visualization',
    align: 'center',
    style: {
      fontSize: '18px',
    },
  },
  colors: ['#007bff'], // Customize the chart color
};

// Initialize the chart
const chart = new ApexCharts(document.querySelector('#chart'), chartOptions);
chart.render();

// Fetch data from API
async function fetchData() {
  try {
    const response = await fetch(API_URL);
    const data = await response.json();
    updateChart(data);
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}

// Update chart with API data
// Update chart with API data
function updateChart(data) {
  // Sort the data by 'created_at' in ascending order
  data.sort((a, b) => new Date(a.created_at) - new Date(b.created_at));

  // Extract sorted categories and values
  const categories = data.map(item => item.created_at); // Extract labels for the x-axis
  const values = data.map(item => item.ph); // Extract values for the series

  chart.updateOptions({
    xaxis: {
      categories: categories, // Update categories
    },
  });

  chart.updateSeries([{
    data: values, // Update series data
  }]);
}


// Initial data fetch and periodic updates
fetchData();
setInterval(fetchData, REFRESH_INTERVAL);
