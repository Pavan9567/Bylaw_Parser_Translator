import { useState } from 'react';
import Upload from './components/Upload';
import Step1View from './components/Step1View';
import Step2View from './components/Step2View';
import { translateSections } from './api';
import './App.css'

function App() {
  const [extracted, setExtracted] = useState(null);
  const [translated, setTranslated] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleTranslate = async () => {
    setLoading(true);
    try {
      const result = await translateSections(extracted);
      setTranslated(result);
    } catch (err) {
      alert("Translation failed");
      console.error(err);
    }
    setLoading(false);
  };

  return (
    <div className="container">
      <div className="header">
        <h1>Bylaw Section Parser & Translator</h1>
        <p>Upload zoning bylaws, extract structured sections, and translate them into plain English</p>
      </div>

      <Upload onExtracted={setExtracted} />

      <Step1View data={extracted} onTranslate={handleTranslate} />

      {loading && <div className='loading'>Translating sections...</div>}

      <Step2View data={translated} />
    </div>
  );
}

export default App
