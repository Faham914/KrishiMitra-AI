# KrishiMitra AI - Requirements Document

## 1. Problem Statement

Indian farmers face significant challenges in determining optimal selling times for their agricultural produce due to volatile market prices. Traditional methods of price prediction rely on historical trends and market intuition, which often lead to suboptimal selling decisions. Farmers frequently sell their crops at unfavorable prices due to lack of accurate forecasting tools, resulting in reduced income and financial instability.

The absence of accessible, localized price prediction systems in regional languages further compounds this problem, particularly for small-scale farmers who need simple, actionable insights to maximize their returns.

## 2. Objective

To develop KrishiMitra AI, an intelligent agricultural price forecasting system that provides farmers and traders with accurate 14-day price predictions for major commodities across different mandis (markets). The system aims to empower users with data-driven selling recommendations and risk assessments to optimize their market decisions.

## 3. Target Users

- **Primary Users**: Small to medium-scale farmers seeking optimal selling times
- **Secondary Users**: Agricultural traders and commission agents
- **Tertiary Users**: Agricultural cooperatives and farmer producer organizations
- **Academic Users**: Students and researchers in agricultural economics

## 4. Scope of the System

### In Scope:
- Price forecasting for 5 major commodities (Tomato, Onion, Potato, Rice, Wheat)
- 14-day forward price predictions
- Multi-language support (English, Hindi, Marathi)
- Risk assessment based on price volatility
- Selling recommendations (SELL/HOLD)
- Interactive web interface with commodity visualization
- Historical price trend analysis

### Out of Scope:
- Real-time market data integration
- Weather data correlation
- Supply chain management
- Payment processing
- Mobile application development
- Multi-user authentication system

## 5. Functional Requirements

1. **Commodity Selection**: System shall allow users to select from 5 predefined commodities
2. **Market Selection**: System shall provide dropdown selection for available mandis
3. **Language Selection**: System shall support interface in English, Hindi, and Marathi
4. **Price Prediction**: System shall generate 14-day price forecasts using time-series analysis
5. **Price Display**: System shall display predicted prices in ₹ per quintal format
6. **Risk Assessment**: System shall calculate and display volatility-based risk levels (Low/Medium/High)
7. **Recommendation Engine**: System shall provide SELL or HOLD recommendations based on predicted vs current price comparison
8. **Visualization**: System shall display interactive price forecast graphs
9. **Commodity Images**: System shall display relevant images for selected commodities
10. **Historical Data Access**: System shall maintain and access historical price data from CSV files
11. **Data Processing**: System shall preprocess and clean historical price data automatically

## 6. Non-Functional Requirements

### Performance:
- Page load time should not exceed 5 seconds under normal usage
- Forecast generation should complete within 10 seconds


### Usability:
- Interface should be intuitive for users with basic digital literacy
- Language switching should be seamless
- Graphs should be clearly readable on desktop and tablet devices

### Reliability:
- Data integrity should be preserved across sessions
- Error handling should provide meaningful feedback to users

### Compatibility:
- Compatible with modern web browsers (Chrome, Firefox, Safari, Edge)
- Responsive design for desktop and tablet viewing
- No mobile-specific optimization required

## 7. Constraints

### Technical Constraints:
- Must use Python as the primary programming language
- Web interface limited to Streamlit framework
- Data storage restricted to local CSV files
- No external database systems allowed
- Time-series forecasting limited to Prophet library
- No machine learning frameworks beyond Prophet

### Operational Constraints:
- Deployment limited to Streamlit Community Cloud
- No custom domain or enterprise hosting
- Limited to publicly available historical price data
- No real-time data feeds or APIs
- Single-user session model (no user accounts)

### Resource Constraints:
- Development time limited to hackathon duration
- Team size limited to 2-4 developers
- No budget for premium services or APIs
- Limited to free-tier cloud resources

## 8. Technology Stack

### Application Layer:
- Streamlit: Python-based web application framework (UI + backend logic)


### Core Libraries:
- **Python**: Core programming language
- **Pandas**: Data manipulation and preprocessing
- **NumPy**: Numerical computations and array operations
- **Prophet**: Time-series forecasting and prediction

### Data Storage:
- **CSV Files**: Local file-based data storage

### Deployment:
- **GitHub**: Version control and code repository
- **Streamlit Community Cloud**: Application hosting and deployment

### Development Tools:
- **Python 3.8+**: Runtime environment
- **Git**: Version control system

## 9. Assumptions

- Historical price data for selected commodities is available and reliable
- Users have basic internet connectivity for accessing the web application
- Price patterns follow predictable seasonal and trend-based behaviors suitable for Prophet forecasting
- Users understand basic agricultural trading concepts (quintal, mandi, price volatility)
- CSV data files contain sufficient historical data (minimum 6 months) for accurate forecasting
- Market conditions remain relatively stable during the forecast period
- Users access the system primarily during business hours
- Language translations are accurate and culturally appropriate

## 10. Future Enhancements

### Short-term Enhancements (3-6 months):
- Integration with government mandi price APIs for real-time data
- Addition of more commodities (sugarcane, cotton, soybeans)
- Weather data correlation for improved forecast accuracy
- SMS-based price alerts for farmers without internet access

### Medium-term Enhancements (6-12 months):
- Mobile application development for Android devices
- User registration and personalized recommendations
- Historical performance tracking and forecast accuracy metrics
- Integration with agricultural news and market updates

### Long-term Enhancements (1-2 years):
- Machine learning model comparison and ensemble forecasting
- Supply chain optimization recommendations
- Integration with agricultural loan and insurance systems
- Expansion to regional markets across India
- Advanced analytics dashboard for agricultural cooperatives
- Blockchain-based price transparency and verification system
