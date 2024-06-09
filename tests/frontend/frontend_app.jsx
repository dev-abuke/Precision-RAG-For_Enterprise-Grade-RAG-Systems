import { render, screen } from '@testing-library/react';
import App from './App';

describe('App', () => {
  const mockProps = {
    prompts: [
      {
        prompt: 'Prompt 1',
        accuracy: 80,
        classification: 'Classification 1',
      },
      {
        prompt: 'Prompt 2',
        accuracy: 95,
        classification: 'Classification 2',
      },
      {
        prompt: 'Prompt 3',
        accuracy: 60,
        classification: 'Classification 3',
      },
    ],
  };

  test('renders prompts correctly', () => {
    render(<App {...mockProps} />);

    expect(screen.getByText('Prompt 1')).toBeInTheDocument();
    expect(screen.getByText('Prompt 2')).toBeInTheDocument();
    expect(screen.getByText('Prompt 3')).toBeInTheDocument();

    expect(screen.getByText('Classification 1')).toBeInTheDocument();
    expect(screen.getByText('Classification 2')).toBeInTheDocument();
    expect(screen.getByText('Classification 3')).toBeInTheDocument();

    expect(screen.getByText('Score : 80')).toBeInTheDocument();
    expect(screen.getByText('Score : 95')).toBeInTheDocument();
    expect(screen.getByText('Score : 60')).toBeInTheDocument();
  });

  test('logs the props correctly', () => {
    const consoleSpy = jest.spyOn(console, 'log');
    render(<App {...mockProps} />);

    expect(consoleSpy).toHaveBeenCalledWith('The props in List Prompt are :: ', mockProps);

    consoleSpy.mockRestore();
  });
});