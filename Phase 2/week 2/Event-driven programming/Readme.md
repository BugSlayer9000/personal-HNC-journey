# Event-Driven Programming (EDP)

Event-Driven Programming (EDP) is a programming paradigm where the flow of the program is controlled by **events** — user actions, sensor outputs, messages, or system signals — rather than a sequential flow of commands.

## Key Concept

In an event-driven model, you don’t write code that says “do A, then B, then C.”  
Instead, you write **handlers** (also called **listeners** or **callbacks**) that wait for something to happen, such as:

- A button click  
- A mouse movement  
- A key press  
- A network message received  
- A timer finishing  

When that event occurs, your handler executes in response.

---

## Core Components

| Component | Description | Python Example |
|------------|--------------|----------------|
| Event Source | The object that generates an event (e.g. button, sensor, socket). | A GUI button in `tkinter` |
| Event Loop | A mechanism that listens for events and dispatches them to the appropriate handler. | `tk.mainloop()` |
| Event Handler (Callback) | A function that executes when a specific event occurs. | `button.bind("<Button-1>", on_click)` |
| Event Object | Data about the event (e.g. mouse position, key pressed). | The `event` parameter in your callback |

---

## HNC Level 7 Focus

At this level, you should be able to:
- Define event-driven programming clearly.  
- Implement simple event-response interactions (e.g. GUI button or keyboard input).  
- Understand how an event loop works.  
- Use Python frameworks such as `tkinter` or `asyncio`.
