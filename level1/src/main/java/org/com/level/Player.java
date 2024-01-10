package org.com.level;

public record Player (String name,
                      Integer goals,
                      Integer speed,
                      Integer assists,
                      Integer passingAccuracy,
                      Integer defensive,
                      Integer jerseyNumber)
{
}
