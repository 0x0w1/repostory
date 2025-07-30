import React, { useState, useEffect, useMemo } from 'react';
import Chart from './Chart';
import RepositorySelector from './RepositorySelector';
import MetricSelector from './MetricSelector';
import { loadRepositoryData, processTimeSeriesData } from '../utils/dataLoader';

const Dashboard = () => {
  const [repositories, setRepositories] = useState([]);
  const [selectedRepos, setSelectedRepos] = useState([]);
  const [selectedMetric, setSelectedMetric] = useState('stars');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const loadData = async () => {
      try {
        setLoading(true);
        const repos = await loadRepositoryData();
        setRepositories(repos);
        
        if (repos.length > 0) {
          setSelectedRepos([repos[0]]);
        }
      } catch (err) {
        setError('Failed to load repository data');
        console.error('Error loading data:', err);
      } finally {
        setLoading(false);
      }
    };

    loadData();
  }, []);

  const chartData = useMemo(() => {
    if (selectedRepos.length === 0) return [];

    const allDates = new Set();
    const repoTimeSeriesData = {};

    selectedRepos.forEach(repo => {
      const timeSeriesData = processTimeSeriesData(repo.starsByDate, repo.forksByDate);
      repoTimeSeriesData[repo.name] = timeSeriesData;
      
      timeSeriesData.forEach(point => {
        allDates.add(point.date);
      });
    });

    const sortedDates = Array.from(allDates).sort();
    
    return sortedDates.map(date => {
      const point = { date };
      
      selectedRepos.forEach(repo => {
        const repoData = repoTimeSeriesData[repo.name];
        const dataPoint = repoData.find(d => d.date === date);
        
        if (dataPoint) {
          point[repo.name] = selectedMetric === 'stars' ? dataPoint.stars : dataPoint.forks;
        } else {
          const previousPoints = repoData.filter(d => d.date < date);
          if (previousPoints.length > 0) {
            const lastPoint = previousPoints[previousPoints.length - 1];
            point[repo.name] = selectedMetric === 'stars' ? lastPoint.stars : lastPoint.forks;
          } else {
            point[repo.name] = 0;
          }
        }
      });
      
      return point;
    });
  }, [selectedRepos, selectedMetric]);

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-4"></div>
          <p className="text-gray-600">Loading repository data...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <div className="text-red-500 text-xl mb-2">⚠️</div>
          <p className="text-gray-600">{error}</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="container mx-auto px-4 py-8">
        <header className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900 mb-2">
            Python Web Frameworks Dashboard
          </h1>
          <p className="text-gray-600">
            Track and compare GitHub stars and forks for popular Python web frameworks
          </p>
        </header>

        <div className="grid grid-cols-1 lg:grid-cols-4 gap-6">
          <div className="lg:col-span-1 space-y-6">
            <MetricSelector
              selectedMetric={selectedMetric}
              onMetricChange={setSelectedMetric}
            />
            
            <RepositorySelector
              repositories={repositories}
              selectedRepos={selectedRepos}
              onRepoToggle={setSelectedRepos}
              maxSelections={5}
            />
          </div>

          <div className="lg:col-span-3">
            <Chart
              data={chartData}
              metric={selectedMetric}
              selectedRepos={selectedRepos}
            />
            
            {selectedRepos.length > 0 && (
              <div className="mt-6 bg-white p-6 rounded-lg shadow-sm border">
                <h3 className="text-lg font-semibold text-gray-900 mb-4">
                  Repository Statistics
                </h3>
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                  {selectedRepos.map((repo) => (
                    <div key={repo.name} className="p-4 bg-gray-50 rounded-lg">
                      <h4 className="font-medium text-gray-900 mb-2">{repo.name}</h4>
                      <div className="space-y-1 text-sm text-gray-600">
                        <p>⭐ {repo.totalStars.toLocaleString()} stars</p>
                        <p>🔀 {Object.values(repo.forksByDate).reduce((sum, forks) => sum + forks, 0).toLocaleString()} forks</p>
                        <p className="text-xs">Updated: {new Date(repo.fetchedAt).toLocaleDateString()}</p>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;