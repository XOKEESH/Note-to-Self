document.addEventListener('DOMContentLoaded', function () {
    var moodDataElement = document.getElementById('moodData');
    console.log(moodDataElement)
    if (moodDataElement) {
        try {
            var moodData = JSON.parse(moodDataElement.textContent.trim());
            console.log(moodData); // Log the parsed data to verify it
            
            // Proceed to use the parsed data in your chart setup
            var ctx = document.getElementById('moodChart').getContext('2d');
            var chart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: ['Bad', 'Not Great', 'Okay', 'Good', 'Great'],
                    datasets: [{
                        label: 'Mood Distribution This Week',
                        data: [
                            moodData.bad || 0,
                            moodData.not_great || 0,
                            moodData.okay || 0,
                            moodData.good || 0,
                            moodData.great || 0
                        ],
                        backgroundColor: ['#f44336', '#ff9800', '#ffeb3b', '#4caf50', '#2196f3'],
                    }]
                },
                options: {
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        } catch (e) {
            console.error('Error parsing mood data:', e);
        }
    } else {
        console.warn('Mood data element not found.');
    }
});









