import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

const DestinationList = () => {
    const [destinations, setDestinations] = useState([]);
    const [loading, setLoading] = useState(true);

    const [viewMode, setViewMode] = useState('grid'); // 'grid' or 'table'

    const fetchDestinations = async () => {
        try {
            const response = await axios.get('http://localhost:5000/destinations');
            setDestinations(response.data);
            setLoading(false);
        } catch (error) {
            console.error('Error fetching destinations:', error);
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchDestinations();
    }, []);

    const handleDelete = async (id) => {
        if (window.confirm('Are you sure you want to delete this destination?')) {
            try {
                await axios.delete(`http://localhost:5000/destinations/${id}`);
                // Refresh list
                fetchDestinations(); 
            } catch (error) {
                console.error('Error deleting destination:', error);
                alert('Failed to delete destination');
            }
        }
    };

    if (loading) return <div>Loading...</div>;

    return (
        <div className="container">
            <h2>All Destinations</h2>
            
            <div style={{display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px'}}>
                <Link to="/create" className="btn btn-primary">+ Add New Destination</Link>
                
                <div>
                   <button 
                        className={`btn ${viewMode === 'grid' ? 'btn-primary' : 'btn-secondary'}`} 
                        onClick={() => setViewMode('grid')}
                        style={{marginRight: '10px'}}
                    >
                        Grid View
                    </button>
                    <button 
                        className={`btn ${viewMode === 'table' ? 'btn-primary' : 'btn-secondary'}`} 
                        onClick={() => setViewMode('table')}
                    >
                        Table View
                    </button>
                </div>
            </div>
            
            {viewMode === 'grid' ? (
                <div className="grid">
                    {destinations.map(dest => (
                        <div key={dest.id} className="card">
                            <img src={dest.image} alt={dest.destination} className="card-img" />
                            <div className="card-body">
                                <h3>{dest.destination}</h3>
                                <p className="text-gray">{dest.country}</p>
                                <p className="rating">⭐ {dest.rating}</p>
                                <div className="actions">
                                    <Link to={`/edit/${dest.id}`} className="btn btn-secondary">Edit</Link>
                                    <button onClick={() => handleDelete(dest.id)} className="btn btn-danger">Delete</button>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
            ) : (
                <div className="table-container">
                    <table className="table">
                        <thead>
                            <tr>
                                <th>Image</th>
                                <th>Destination</th>
                                <th>Country</th>
                                <th>Rating</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                            {destinations.map(dest => (
                                <tr key={dest.id}>
                                    <td><img src={dest.image} alt={dest.destination} className="table-img" /></td>
                                    <td>{dest.destination}</td>
                                    <td>{dest.country}</td>
                                    <td>⭐ {dest.rating}</td>
                                    <td>
                                        <Link to={`/edit/${dest.id}`} className="btn btn-secondary" style={{marginRight: '5px'}}>Edit</Link>
                                        <button onClick={() => handleDelete(dest.id)} className="btn btn-danger">Delete</button>
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            )}
            
            {destinations.length === 0 && <p>No destinations found.</p>}
        </div>
    );
};

export default DestinationList;
