class Attendee
  def initialize(height)
    @height = height
  end

  def height
    return @height
  end

  def pass_id
    return @issue_pass
  end

  def issue_pass!(pass_id)
    @issue_pass = pass_id
  end

  def revoke_pass!
    @issue_pass = nil
  end
end
