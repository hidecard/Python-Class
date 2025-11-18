# POS System Improvements TODO

## 1. Improve Dashboard UI
- [ ] Redesign dashboard_frame.py with grid layout and better styling
- [ ] Add "POS Sales" button to access the new sales interface
- [ ] Arrange buttons in a more professional layout

## 2. Redesign Safe Page as POS Sales Screen
- [ ] Rename safe_page_frame.py to pos_sales_frame.py
- [ ] Implement item selection via list or barcode search
- [ ] Add cart functionality with quantity management
- [ ] Calculate and display total amount
- [ ] Implement checkout process that saves to sales table
- [ ] Add staff selection for sales

## 3. Update Main Application
- [ ] Update pos_system.py to use POSFrame instead of SafePageFrame
- [ ] Add POSFrame to frames dictionary
- [ ] Update show_frame logic for POS

## 4. Testing
- [ ] Test dashboard navigation
- [ ] Test POS sales functionality (add items, calculate total, checkout)
- [ ] Verify database saves sales correctly
