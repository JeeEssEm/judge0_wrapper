from pydantic import BaseModel, Field, field_validator


class CreateSubmissionSchema(BaseModel):
    task_id: int
    source_code: str = Field(..., min_length=1, max_length=100000, description="Source code")
    language_id: str

    stdin: str | None = Field(default=None, max_length=10000, description="stdin")
    compiler_options: str | None = Field(default=None, max_length=512, description="Compiler options")
    command_line_arguments: str | None = Field(default=None, max_length=512, description="CMD args")

    @field_validator("source_code")
    def validate_source_code(cls, v):
        if len(v.strip()) == 0:
            raise ValueError("Source code cannot be empty")
        return v

    @field_validator("compiler_options")
    def validate_compiler_options(cls, v):
        if v and len(v) > 512:
            raise ValueError("Compiler options too long")
        return v

    @field_validator("command_line_arguments")
    def validate_command_line_args(cls, v):
        if v and len(v) > 512:
            raise ValueError("Command line arguments too long")
        return v


class SubmissionSchema(BaseModel):
    token: str
    stdout: str | None
    stderr: str | None
    message: str | None
    compile_output: str | None
    status: str | None
    accepted: bool

    @classmethod
    def from_json(cls, data):
        return cls(
            token=data["token"],
            stdout=data["stdout"],
            stderr=data["stderr"],
            message=data["message"],
            compile_output=data["compile_output"],
            status=data["status"]["description"],
            accepted=data["status"]["description"] == "Accepted"
        )
