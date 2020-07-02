import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import Home from '../components/Home/Home';

test('renders Home component', () => {
  const { getByText, getByTestId } = render(<Home />);
  expect(getByText("Let's check your pulse!")).toBeInTheDocument();
  expect(
    getByText('Place your finger over your camera for 15-30 seconds')
  ).toBeInTheDocument();
  fireEvent.click(getByTestId('camera-button'));
  fireEvent.click(getByTestId('upload-button'));
  fireEvent.click(getByTestId('sign-out-button'));
});
