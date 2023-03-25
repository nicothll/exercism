class Attendee
  def initialize(height)
    @height = height
  end

  def issue_pass!(pass_id)
    @pass_id = pass_id
  end

  def revoke_pass!
    @pass_id = nil
  end

  def has_pass?
    if @pass_id == nil
      false
    else
      true
    end
  end

  def fits_ride?(ride_minimum_height)
    return @height >= ride_minimum_height
  end

  def allowed_to_ride?(ride_minimum_height)
    return has_pass? == fits_ride?(ride_minimum_height)
  end
end
