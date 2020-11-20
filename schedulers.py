from des import SchedulerDES
from event import Event, EventTypes
from process import Process, ProcessStates


class FCFS(SchedulerDES):
    def scheduler_func(self, cur_event):
        # return the first process, the one which just arrived
        return self.processes[cur_event.process_id]

    def dispatcher_func(self, cur_process):
        # run the process for remaining time and return DONE event
        cur_process.process_state = ProcessStates.RUNNING
        service_time = cur_process.run_for(cur_process.remaining_time, self.time)
        cur_process.process_state = ProcessStates.TERMINATED
        new_event = Event(process_id=cur_process.process_id, event_time=self.time + service_time,
                    event_type=EventTypes.PROC_CPU_DONE)
        return new_event


class SJF(SchedulerDES):
    def scheduler_func(self, cur_event):
        # from processes that are ready select the one with shortest time
        shortest_process_i = None;
        for i in range(len(self.processes)):
            if self.processes[i].process_state == ProcessStates.READY:
                # let first READY process be the shortest
                if shortest_process_i == None:
                    shortest_process_i = i
                # if current process is shorter than the selected one, replace it
                elif self.processes[i].remaining_time < self.processes[shortest_process_i].remaining_time:
                    shortest_process_i = i
        return self.processes[shortest_process_i]
            

    def dispatcher_func(self, cur_process):
        # run the process for remaining time and return DONE event
        cur_process.process_state = ProcessStates.RUNNING
        service_time = cur_process.run_for(cur_process.remaining_time, self.time)
        cur_process.process_state = ProcessStates.TERMINATED
        new_event = Event(process_id=cur_process.process_id, event_time=self.time + service_time,
                    event_type=EventTypes.PROC_CPU_DONE)
        return new_event


class RR(SchedulerDES):
    def scheduler_func(self, cur_event):
        return self.processes[cur_event.process_id]


    def dispatcher_func(self, cur_process):
        # run process for quantum time
        cur_process.process_state = ProcessStates.RUNNING
        service_time = cur_process.run_for(self.quantum, self.time)

        # set relevant state and create appropriate event
        if cur_process.remaining_time == 0: 
            cur_process.process_state = ProcessStates.TERMINATED
            new_event = Event(process_id=cur_process.process_id, event_time=self.time + service_time,
                        event_type=EventTypes.PROC_CPU_DONE)
        else:
            cur_process.process_state = ProcessStates.READY
            new_event = Event(process_id=cur_process.process_id, event_time=self.time + service_time,
                        event_type=EventTypes.PROC_CPU_REQ)

        return new_event


class SRTF(SchedulerDES):
    def scheduler_func(self, cur_event):
        # from processes that are ready select the one with shortest remaining time
        shortest_process_i = None;
        for i in range(len(self.processes)):
            if self.processes[i].process_state == ProcessStates.READY:
                # let first READY process be the shortest
                if shortest_process_i == None:
                    shortest_process_i = i
                # if current process is shorter than the selected one, replace it
                elif self.processes[i].remaining_time < self.processes[shortest_process_i].remaining_time:
                    shortest_process_i = i
        return self.processes[shortest_process_i]

    def dispatcher_func(self, cur_process):
        # determine quantum time and run
        quantum_time = self.next_event_time() - self.time
        cur_process.process_state = ProcessStates.RUNNING
        service_time = cur_process.run_for(quantum_time, self.time)

        # set relevant state and create event
        if cur_process.remaining_time == 0: 
            cur_process.process_state = ProcessStates.TERMINATED
            new_event = Event(process_id=cur_process.process_id, event_time=self.time + service_time,
                        event_type=EventTypes.PROC_CPU_DONE)
        else:
            cur_process.process_state = ProcessStates.READY
            new_event = Event(process_id=cur_process.process_id, event_time=self.time + service_time,
                        event_type=EventTypes.PROC_CPU_REQ)

        return new_event
        