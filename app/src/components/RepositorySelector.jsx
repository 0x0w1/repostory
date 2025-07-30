import React from 'react';
import { formatNumber } from '../utils/dataLoader';

const RepositorySelector = ({ repositories, selectedRepos, onRepoToggle, maxSelections = 5 }) => {
  const handleToggle = (repo) => {
    const isSelected = selectedRepos.some(selected => selected.name === repo.name);
    
    if (isSelected) {
      onRepoToggle(selectedRepos.filter(selected => selected.name !== repo.name));
    } else if (selectedRepos.length < maxSelections) {
      onRepoToggle([...selectedRepos, repo]);
    }
  };

  return (
    <div className="bg-white p-6 rounded-lg shadow-sm border">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-semibold text-gray-900">Select Repositories</h3>
        <span className="text-sm text-gray-500">
          {selectedRepos.length}/{maxSelections} selected
        </span>
      </div>
      
      <div className="space-y-2 max-h-96 overflow-y-auto">
        {repositories.map((repo) => {
          const isSelected = selectedRepos.some(selected => selected.name === repo.name);
          const canSelect = selectedRepos.length < maxSelections || isSelected;
          
          return (
            <div
              key={repo.name}
              className={`flex items-center justify-between p-3 rounded-lg border cursor-pointer transition-colors ${
                isSelected
                  ? 'bg-blue-50 border-blue-200'
                  : canSelect
                  ? 'hover:bg-gray-50 border-gray-200'
                  : 'opacity-50 cursor-not-allowed border-gray-200'
              }`}
              onClick={() => canSelect && handleToggle(repo)}
            >
              <div className="flex items-center space-x-3">
                <input
                  type="checkbox"
                  checked={isSelected}
                  onChange={() => {}}
                  className="w-4 h-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
                  disabled={!canSelect}
                />
                <div>
                  <p className="font-medium text-gray-900">{repo.name}</p>
                  <p className="text-sm text-gray-500">
                    ⭐ {formatNumber(repo.totalStars)} stars
                  </p>
                </div>
              </div>
              <div className="text-xs text-gray-400">
                {new Date(repo.fetchedAt).toLocaleDateString()}
              </div>
            </div>
          );
        })}
      </div>
      
      {selectedRepos.length > 0 && (
        <div className="mt-4 pt-4 border-t">
          <p className="text-sm text-gray-600 mb-2">Selected repositories:</p>
          <div className="flex flex-wrap gap-2">
            {selectedRepos.map((repo) => (
              <span
                key={repo.name}
                className="inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-blue-100 text-blue-800"
              >
                {repo.name}
                <button
                  onClick={() => handleToggle(repo)}
                  className="ml-1 text-blue-600 hover:text-blue-800"
                >
                  ×
                </button>
              </span>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default RepositorySelector;