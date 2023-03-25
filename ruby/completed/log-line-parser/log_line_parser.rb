class LogLineParser
  def initialize(line)
    @line = line
    @partition = @line.partition(':')
  end

  def message
    @partition[-1].strip()
  end

  def log_level
    @partition[0].gsub(/[\[\]]/, '').downcase
  end

  def reformat
    "#{message} (#{log_level})"
  end
end
