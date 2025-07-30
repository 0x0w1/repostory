export const loadRepositoryData = async () => {
  try {
    const response = await fetch('../repo_data/');
    const text = await response.text();
    
    const fileNames = [];
    const parser = new DOMParser();
    const doc = parser.parseFromString(text, 'text/html');
    const links = doc.querySelectorAll('a[href$=".json"]');
    
    links.forEach(link => {
      const href = link.getAttribute('href');
      if (href && href.endsWith('.json')) {
        fileNames.push(href);
      }
    });

    const repositories = [];
    
    for (const fileName of fileNames) {
      try {
        const response = await fetch(`../repo_data/${fileName}`);
        const data = await response.json();
        
        const repoName = fileName.replace('.json', '').replace(/_/g, '/');
        
        repositories.push({
          name: repoName,
          fileName: fileName,
          totalStars: data.total_stars,
          fetchedAt: data.fetched_at,
          starsByDate: data.stars_by_date || {},
          forksByDate: data.forks_by_date || {}
        });
      } catch (error) {
        console.warn(`Failed to load ${fileName}:`, error);
      }
    }

    return repositories.sort((a, b) => b.totalStars - a.totalStars);
  } catch (error) {
    console.error('Failed to load repository data:', error);
    return [];
  }
};

export const processTimeSeriesData = (starsByDate, forksByDate) => {
  const dates = new Set([...Object.keys(starsByDate), ...Object.keys(forksByDate)]);
  const sortedDates = Array.from(dates).sort();
  
  let cumulativeStars = 0;
  let cumulativeForks = 0;
  
  const timeSeriesData = sortedDates.map(date => {
    cumulativeStars += starsByDate[date] || 0;
    cumulativeForks += forksByDate[date] || 0;
    
    return {
      date,
      stars: cumulativeStars,
      forks: cumulativeForks,
      dailyStars: starsByDate[date] || 0,
      dailyForks: forksByDate[date] || 0
    };
  });
  
  return timeSeriesData;
};

export const formatDate = (dateString) => {
  const date = new Date(dateString);
  return date.toLocaleDateString('en-US', { 
    year: 'numeric', 
    month: 'short', 
    day: 'numeric' 
  });
};

export const formatNumber = (num) => {
  if (num >= 1000000) {
    return (num / 1000000).toFixed(1) + 'M';
  } else if (num >= 1000) {
    return (num / 1000).toFixed(1) + 'K';
  }
  return num.toString();
};