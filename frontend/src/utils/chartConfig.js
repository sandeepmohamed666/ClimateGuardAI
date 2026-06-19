// src/config/chartConfig.js


export const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,


  plugins: {
    legend: {
      position: "top",
      labels: {
        color: "#E2E8F0",
        font: {
          size: 12,
          weight: "bold",
        },
      },
    },


    tooltip: {
      backgroundColor: "#1E293B",
      titleColor: "#FFFFFF",
      bodyColor: "#CBD5E1",
      borderColor: "#38BDF8",
      borderWidth: 1,
      padding: 10,
      cornerRadius: 8,
    },
  },


  scales: {
    x: {
      grid: {
        color: "rgba(255,255,255,0.08)",
      },
      ticks: {
        color: "#CBD5E1",
      },
    },


    y: {
      beginAtZero: true,
      grid: {
        color: "rgba(255,255,255,0.08)",
      },
      ticks: {
        color: "#CBD5E1",
      },
    },
  },
};


export const climateColors = {
  temperature: "#EF4444",
  humidity: "#3B82F6",
  rainfall: "#06B6D4",
  airQuality: "#F59E0B",
  pressure: "#8B5CF6",
  visibility: "#10B981",
  uvIndex: "#F97316",
};


export const chartDataset = (
  label,
  data,
  borderColor,
  backgroundColor
) => ({
  label,
  data,
  borderColor,
  backgroundColor,
  fill: true,
  tension: 0.4,
  borderWidth: 2,
  pointRadius: 3,
  pointHoverRadius: 5,
}); 


