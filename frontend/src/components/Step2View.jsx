import JSONPretty from "react-json-pretty";
import "react-json-pretty/themes/monikai.css";
import { downloadJSON } from "../utils/downloadJson";

export default function Step2View({ data }) {
    if (!data) return null;

    return (
        <div className="card">
            <div className="step-title">
                <span className="step-badge">STEP 2</span>
                <h2>Translate Sections</h2>
            </div>

            <button style={{ marginBottom: "10px" }} onClick={() => downloadJSON(data, "bylaw_translated_sections.json")}>Download</button>

            <div className="json-box">
                <JSONPretty data={data} />
            </div>
        </div>
    );
}