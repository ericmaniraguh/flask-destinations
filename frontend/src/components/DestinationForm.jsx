import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useNavigate, useParams } from 'react-router-dom';

const DestinationForm = () => {
    const [formData, setFormData] = useState({
        destination: '',
        country: '',
        rating: '',
        image: ''
    });
    const navigate = useNavigate();
    const { id } = useParams();
    const isEditMode = !!id;

    useEffect(() => {
        if (isEditMode) {
            fetchDestination();
        }
    }, [id]);

    const fetchDestination = async () => {
        try {
            const response = await axios.get(`http://localhost:5000/destinations/${id}`);
            setFormData(response.data);
        } catch (error) {
            console.error('Error fetching destination:', error);
        }
    };

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            if (isEditMode) {
                await axios.put(`http://localhost:5000/destinations/${id}`, formData);
            } else {
                await axios.post('http://localhost:5000/destinations', formData);
            }
            navigate('/');
        } catch (error) {
            console.error('Error saving destination:', error);
            alert('Failed to save destination');
        }
    };

    return (
        <div className="container">
            <h2>{isEditMode ? 'Edit Destination' : 'Create New Destination'}</h2>
            <form onSubmit={handleSubmit} className="form">
                <div className="form-group">
                    <label>Destination Name:</label>
                    <input
                        type="text"
                        name="destination"
                        value={formData.destination}
                        onChange={handleChange}
                        required
                    />
                </div>
                <div className="form-group">
                    <label>Country:</label>
                    <input
                        type="text"
                        name="country"
                        value={formData.country}
                        onChange={handleChange}
                        required
                    />
                </div>
                <div className="form-group">
                    <label>Rating (0-5):</label>
                    <input
                        type="number"
                        name="rating"
                        step="0.1"
                        min="0"
                        max="5"
                        value={formData.rating}
                        onChange={handleChange}
                        required
                    />
                </div>
                <div className="form-group">
                    <label>Image URL:</label>
                    <input
                        type="url"
                        name="image"
                        value={formData.image}
                        onChange={handleChange}
                        required
                    />
                </div>
                <button type="submit" className="btn btn-primary">
                    {isEditMode ? 'Update' : 'Create'}
                </button>
                <button type="button" onClick={() => navigate('/')} className="btn btn-secondary" style={{marginLeft: '10px'}}>
                    Cancel
                </button>
            </form>
        </div>
    );
};

export default DestinationForm;
