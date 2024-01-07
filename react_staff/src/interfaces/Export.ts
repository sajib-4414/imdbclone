export interface Export {
  id: number;
  creator: User;
  file_name?:string;
  status: ExportStatus;
  task_id: string;
  description:string;
  created_at: Date;
  updated_at:Date;

}
export enum ExportStatus {
  QUEUED = 'queued',
  IN_PROGRESS = 'in_progress',
  COMPLETED = 'completed',
  FAILED = 'failed',
}

export interface User {
  id: number;
  email: string;
  username: string;
}

export const statusDisplayNames: Record<ExportStatus, string> = {
  [ExportStatus.QUEUED]: 'Queued',
  [ExportStatus.IN_PROGRESS]: 'In Progress',
  [ExportStatus.COMPLETED]: 'Completed',
  [ExportStatus.FAILED]: 'Failed',
};